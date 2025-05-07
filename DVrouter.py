####################################################
# DVrouter.py
# Name:
# HUID:
#####################################################

from packet import Packet
from router import Router
import json


class DVrouter(Router):
    """Distance vector routing protocol implementation."""

    def __init__(self, addr, heartbeat_time):
        Router.__init__(self, addr)  # Initialize base class - DO NOT REMOVE
        self.heartbeat_time = heartbeat_time
        self.last_time = 0
        self.distance_vector = {self.addr: 0}  # Distance to self is 0
        self.forwarding_table = {}  # Maps destination to (port, cost)
        self.neighbors = {}  # Maps port to (neighbor address, cost)

    def handle_packet(self, port, packet):
        """Process incoming packet."""
        if packet.is_traceroute:
            # Forward traceroute packets based on forwarding table
            if packet.dst_addr in self.forwarding_table:
                next_port, _ = self.forwarding_table[packet.dst_addr]
                self.send(next_port, packet)
        else:
            # Handle routing packets
            received_dv = json.loads(packet.content)
            updated = False
            for dest, cost in received_dv.items():
                new_cost = self.neighbors[port][1] + cost
                if dest not in self.distance_vector or new_cost < self.distance_vector[dest]:
                    self.distance_vector[dest] = new_cost
                    self.forwarding_table[dest] = (port, new_cost)
                    updated = True
            if updated:
                self.broadcast_distance_vector()

    def handle_new_link(self, port, endpoint, cost):
        """Handle new link."""
        self.neighbors[port] = (endpoint, cost)
        self.distance_vector[endpoint] = cost
        self.forwarding_table[endpoint] = (port, cost)
        self.broadcast_distance_vector()

    def handle_remove_link(self, port):
        """Handle removed link."""
        if port in self.neighbors:
            endpoint, _ = self.neighbors.pop(port)
            self.distance_vector.pop(endpoint, None)
            self.forwarding_table = {dest: (p, c) for dest, (p, c) in self.forwarding_table.items() if p != port}
            self.broadcast_distance_vector()

    def handle_time(self, time_ms):
        """Handle current time."""
        if time_ms - self.last_time >= self.heartbeat_time:
            self.last_time = time_ms
            self.broadcast_distance_vector()

    def broadcast_distance_vector(self):
        """Broadcast the distance vector of this router to neighbors."""
        content = json.dumps(self.distance_vector)
        for port in self.neighbors:
            packet = self.create_routing_packet(content)
            self.send(port, packet)

    def create_routing_packet(self, content):
        """Create a routing packet."""
        packet = Packet(kind=Packet.ROUTING, src_addr=self.addr, dst_addr="255.255.255.255", content=content)
        return packet

    def __repr__(self):
        """Representation for debugging in the network visualizer."""
        return f"DVrouter(addr={self.addr}, dv={self.distance_vector})"
