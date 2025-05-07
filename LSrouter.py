####################################################
# LSrouter.py
# Name:
# HUID:
#####################################################

from packet import Packet
from router import Router
import json
import networkx as nx


class LSrouter(Router):
    """Link state routing protocol implementation."""

    def __init__(self, addr, heartbeat_time):
        Router.__init__(self, addr)  # Initialize base class - DO NOT REMOVE
        self.heartbeat_time = heartbeat_time
        self.last_time = 0
        self.link_state = {}  # Maps router to its link state (neighbors and costs)
        self.sequence_numbers = {}  # Maps router to its latest sequence number
        self.sequence_numbers[self.addr] = 0  # Initialize sequence number for this router
        self.graph = nx.DiGraph()  # Network graph for shortest path computation
        self.forwarding_table = {}  # Maps destination to (port, cost)

    def handle_packet(self, port, packet):
        """Process incoming packet."""
        if packet.is_traceroute:
            # Forward traceroute packets based on forwarding table
            if packet.dst_addr in self.forwarding_table:
                next_port, _ = self.forwarding_table[packet.dst_addr]
                self.send(next_port, packet)
        else:
            # Handle routing packets
            received_ls = json.loads(packet.content)
            src, seq_num, neighbors = received_ls["src"], received_ls["seq_num"], received_ls["neighbors"]
            if src not in self.sequence_numbers or seq_num > self.sequence_numbers[src]:
                self.sequence_numbers[src] = seq_num
                self.link_state[src] = neighbors
                self.update_graph()
                self.broadcast_link_state(packet.content)

    def handle_new_link(self, port, endpoint, cost):
        """Handle new link."""
        self.link_state.setdefault(self.addr, {})[endpoint] = cost
        self.update_graph()
        self.broadcast_link_state()

    def handle_remove_link(self, port):
        """Handle removed link."""
        if self.addr in self.link_state:
            for neighbor, cost in list(self.link_state[self.addr].items()):
                if neighbor == port:
                    del self.link_state[self.addr][neighbor]
        self.update_graph()
        self.broadcast_link_state()

    def handle_time(self, time_ms):
        """Handle current time."""
        if time_ms - self.last_time >= self.heartbeat_time:
            self.last_time = time_ms
            self.broadcast_link_state()

    def update_graph(self):
        """Update the network graph based on the current link state."""
        self.graph.clear()
        for router, neighbors in self.link_state.items():
            for neighbor, cost in neighbors.items():
                self.graph.add_edge(router, neighbor, weight=cost)
        self.update_forwarding_table()

    def update_forwarding_table(self):
        """Update the forwarding table based on the shortest paths in the graph."""
        self.forwarding_table.clear()
        try:
            paths = nx.single_source_dijkstra_path(self.graph, self.addr)
            for dest, path in paths.items():
                if len(path) > 1:
                    next_hop = path[1]
                    for port, link in self.links.items():
                        if link.e1 == next_hop or link.e2 == next_hop:
                            self.forwarding_table[dest] = (port, self.graph[self.addr][next_hop]["weight"])
        except nx.NetworkXNoPath:
            pass

    def broadcast_link_state(self, content=None):
        """Broadcast the link state of this router to all neighbors."""
        if content is None:
            content = json.dumps({
                "src": self.addr,
                "seq_num": self.sequence_numbers.get(self.addr, 0) + 1,
                "neighbors": self.link_state.get(self.addr, {})
            })
            self.sequence_numbers[self.addr] += 1
        for neighbor in self.link_state.get(self.addr, {}):
            port = self.get_port_for_neighbor(neighbor)
            if port is not None:
                packet = self.create_routing_packet(content, neighbor)
                self.send(port, packet)

    def create_routing_packet(self, content, dst_addr):
        """Create a routing packet."""
        packet = Packet(kind=Packet.ROUTING, src_addr=self.addr, dst_addr=dst_addr, content=content)
        return packet

    def get_port_for_neighbor(self, neighbor):
        """Get the port for a given neighbor."""
        for port, link in self.links.items():
            if link.e1 == neighbor or link.e2 == neighbor:
                return port
        return None

    def __repr__(self):
        """Representation for debugging in the network visualizer."""
        return f"LSrouter(addr={self.addr}, link_state={self.link_state})"
