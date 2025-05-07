# Testing Link State routing implementation

## 1. Testing /home/kineNg/Documents/ComputerNetwork/routing/06_pg242_net_events.json with LSrouter

a -> a: ['a', 'A', 'a']
a -> b: ['a', 'A', 'E', 'B', 'b']
a -> c: ['a', 'A', 'E', 'B', 'C', 'c']
a -> d: [] Incorrect Route
a -> e: ['a', 'A', 'E', 'e']
a -> f: ['a', 'A', 'E', 'F', 'f']
b -> a: ['b', 'B', 'E', 'A', 'a']
b -> b: ['b', 'B', 'b']
b -> c: ['b', 'B', 'C', 'c']
b -> d: ['b', 'B', 'E', 'D', 'd']
b -> e: ['b', 'B', 'E', 'e']
b -> f: ['b', 'B', 'E', 'F', 'f']
c -> a: ['c', 'C', 'B', 'E', 'A', 'a']
c -> b: ['c', 'C', 'B', 'b']
c -> c: ['c', 'C', 'c']
c -> d: ['c', 'C', 'B', 'E', 'D', 'd']
c -> e: ['c', 'C', 'B', 'E', 'e']
c -> f: ['c', 'C', 'B', 'E', 'F', 'f']
d -> a: [] Incorrect Route
d -> b: ['d', 'D', 'E', 'B', 'b']
d -> c: ['d', 'D', 'E', 'B', 'C', 'c']
d -> d: ['d', 'D', 'd']
d -> e: ['d', 'D', 'E', 'e']
d -> f: ['d', 'D', 'E', 'F', 'f']
e -> a: ['e', 'E', 'A', 'a']
e -> b: ['e', 'E', 'B', 'b']
e -> c: ['e', 'E', 'B', 'C', 'c']
e -> d: ['e', 'E', 'D', 'd']
e -> e: ['e', 'E', 'e']
e -> f: ['e', 'E', 'F', 'f']
f -> a: ['f', 'F', 'E', 'A', 'a']
f -> b: ['f', 'F', 'E', 'B', 'b']
f -> c: ['f', 'F', 'E', 'B', 'C', 'c']
f -> d: ['f', 'F', 'E', 'D', 'd']
f -> e: ['f', 'F', 'E', 'e']
f -> f: ['f', 'F', 'f']

FAILURE: Not all routes are correct

---

## 2. Testing /home/kineNg/Documents/ComputerNetwork/routing/03_pg244_net.json with LSrouter

a -> a: ['a', 'A', 'a']
a -> b: ['a', 'A', 'B', 'b']
a -> c: ['a', 'A', 'C', 'c']
a -> d: ['a', 'A', 'C', 'D', 'd']
a -> e: ['a', 'A', 'E', 'e']
a -> f: ['a', 'A', 'F', 'f']
a -> g: ['a', 'A', 'F', 'G', 'g']
b -> a: ['b', 'B', 'A', 'a']
b -> b: ['b', 'B', 'b']
b -> c: ['b', 'B', 'C', 'c']
b -> d: ['b', 'B', 'C', 'D', 'd']
b -> e: ['b', 'B', 'A', 'E', 'e']
b -> f: ['b', 'B', 'A', 'F', 'f']
b -> g: ['b', 'B', 'A', 'F', 'G', 'g']
c -> a: ['c', 'C', 'A', 'a']
c -> b: ['c', 'C', 'B', 'b']
c -> c: ['c', 'C', 'c']
c -> d: ['c', 'C', 'D', 'd']
c -> e: ['c', 'C', 'A', 'E', 'e']
c -> f: ['c', 'C', 'A', 'F', 'f']
c -> g: ['c', 'C', 'D', 'G', 'g']
d -> a: ['d', 'D', 'C', 'A', 'a']
d -> b: ['d', 'D', 'C', 'B', 'b']
d -> c: ['d', 'D', 'C', 'c']
d -> d: ['d', 'D', 'd']
d -> e: ['d', 'D', 'C', 'A', 'E', 'e']
d -> f: ['d', 'D', 'G', 'F', 'f']
d -> g: ['d', 'D', 'G', 'g']
e -> a: ['e', 'E', 'A', 'a']
e -> b: ['e', 'E', 'A', 'B', 'b']
e -> c: ['e', 'E', 'A', 'C', 'c']
e -> d: ['e', 'E', 'A', 'C', 'D', 'd']
e -> e: ['e', 'E', 'e']
e -> f: ['e', 'E', 'A', 'F', 'f']
e -> g: ['e', 'E', 'A', 'F', 'G', 'g']
f -> a: ['f', 'F', 'A', 'a']
f -> b: ['f', 'F', 'A', 'B', 'b']
f -> c: ['f', 'F', 'A', 'C', 'c']
f -> d: ['f', 'F', 'G', 'D', 'd']
f -> e: ['f', 'F', 'A', 'E', 'e']
f -> f: ['f', 'F', 'f']
f -> g: ['f', 'F', 'G', 'g']
g -> a: ['g', 'G', 'F', 'A', 'a']
g -> b: ['g', 'G', 'D', 'C', 'B', 'b']
g -> c: ['g', 'G', 'D', 'C', 'c']
g -> d: ['g', 'G', 'D', 'd']
g -> e: ['g', 'G', 'F', 'A', 'E', 'e']
g -> f: ['g', 'G', 'F', 'f']
g -> g: ['g', 'G', 'g']

SUCCESS: All Routes correct!

---

## 3. Testing /home/kineNg/Documents/ComputerNetwork/routing/01_small_net.json with LSrouter

b -> b: ['b', 'A', 'b']
b -> c: ['b', 'A', 'c']
b -> d: ['b', 'A', 'E', 'd']
c -> b: ['c', 'A', 'b']
c -> c: ['c', 'A', 'c']
c -> d: ['c', 'A', 'E', 'd']
d -> b: ['d', 'E', 'A', 'b']
d -> c: ['d', 'E', 'A', 'c']
d -> d: ['d', 'E', 'd']

SUCCESS: All Routes correct!

---

## 4. Testing /home/kineNg/Documents/ComputerNetwork/routing/04_pg244_net_events.json with LSrouter

a -> a: ['a', 'A', 'a']
a -> b: ['a', 'A', 'B', 'b']
a -> c: ['a', 'A', 'C', 'c']
a -> d: ['a', 'A', 'C', 'D', 'd']
a -> e: ['a', 'A', 'E', 'e']
a -> f: ['a', 'A', 'F', 'f']
a -> g: [] Incorrect Route
b -> a: ['b', 'B', 'A', 'a']
b -> b: ['b', 'B', 'b']
b -> c: ['b', 'B', 'C', 'c']
b -> d: ['b', 'B', 'C', 'D', 'd']
b -> e: ['b', 'B', 'A', 'E', 'e']
b -> f: ['b', 'B', 'A', 'F', 'f']
b -> g: [] Incorrect Route
c -> a: ['c', 'C', 'A', 'a']
c -> b: ['c', 'C', 'B', 'b']
c -> c: ['c', 'C', 'c']
c -> d: ['c', 'C', 'D', 'd']
c -> e: ['c', 'C', 'A', 'E', 'e']
c -> f: ['c', 'C', 'A', 'F', 'f']
c -> g: ['c', 'C', 'D', 'G', 'g']
d -> a: ['d', 'D', 'C', 'A', 'a']
d -> b: ['d', 'D', 'C', 'B', 'b']
d -> c: ['d', 'D', 'C', 'c']
d -> d: ['d', 'D', 'd']
d -> e: [] Incorrect Route
d -> f: ['d', 'D', 'G', 'F', 'f']
d -> g: ['d', 'D', 'G', 'g']
e -> a: ['e', 'E', 'A', 'a']
e -> b: ['e', 'E', 'A', 'B', 'b']
e -> c: ['e', 'E', 'A', 'C', 'c']
e -> d: [] Incorrect Route
e -> e: ['e', 'E', 'e']
e -> f: ['e', 'E', 'A', 'F', 'f']
e -> g: [] Incorrect Route
f -> a: ['f', 'F', 'A', 'a']
f -> b: ['f', 'F', 'A', 'B', 'b']
f -> c: ['f', 'F', 'A', 'C', 'c']
f -> d: ['f', 'F', 'G', 'D', 'd']
f -> e: ['f', 'F', 'A', 'E', 'e']
f -> f: ['f', 'F', 'f']
f -> g: ['f', 'F', 'G', 'g']
g -> a: [] Incorrect Route
g -> b: [] Incorrect Route
g -> c: ['g', 'G', 'D', 'C', 'c']
g -> d: ['g', 'G', 'D', 'd']
g -> e: [] Incorrect Route
g -> f: ['g', 'G', 'F', 'f']
g -> g: ['g', 'G', 'g']

FAILURE: Not all routes are correct

---

## 5. Testing /home/kineNg/Documents/ComputerNetwork/routing/02_small_net_events.json with LSrouter

b -> b: ['b', 'A', 'b']
b -> c: ['b', 'A', 'c']
b -> d: ['b', 'A', 'E', 'd']
c -> b: ['c', 'A', 'b']
c -> c: ['c', 'A', 'c']
c -> d: ['c', 'A', 'E', 'd']
d -> b: ['d', 'E', 'A', 'b']
d -> c: ['d', 'E', 'A', 'c']
d -> d: ['d', 'E', 'd']

SUCCESS: All Routes correct!

---

## 6. Testing /home/kineNg/Documents/ComputerNetwork/routing/05_pg242_net.json with LSrouter

a -> a: ['a', 'A', 'a']
a -> b: ['a', 'A', 'E', 'B', 'b']
a -> c: ['a', 'A', 'E', 'B', 'C', 'c']
a -> d: ['a', 'A', 'E', 'D', 'd']
a -> e: ['a', 'A', 'E', 'e']
a -> f: ['a', 'A', 'E', 'F', 'f']
b -> a: ['b', 'B', 'E', 'A', 'a']
b -> b: ['b', 'B', 'b']
b -> c: ['b', 'B', 'C', 'c']
b -> d: ['b', 'B', 'E', 'D', 'd']
b -> e: ['b', 'B', 'E', 'e']
b -> f: ['b', 'B', 'E', 'F', 'f']
c -> a: ['c', 'C', 'B', 'E', 'A', 'a']
c -> b: ['c', 'C', 'B', 'b']
c -> c: ['c', 'C', 'c']
c -> d: ['c', 'C', 'B', 'E', 'D', 'd']
c -> e: ['c', 'C', 'B', 'E', 'e']
c -> f: ['c', 'C', 'B', 'E', 'F', 'f']
d -> a: ['d', 'D', 'E', 'A', 'a']
d -> b: ['d', 'D', 'E', 'B', 'b']
d -> c: ['d', 'D', 'E', 'B', 'C', 'c']
d -> d: ['d', 'D', 'd']
d -> e: ['d', 'D', 'E', 'e']
d -> f: ['d', 'D', 'E', 'F', 'f']
e -> a: ['e', 'E', 'A', 'a']
e -> b: ['e', 'E', 'B', 'b']
e -> c: ['e', 'E', 'B', 'C', 'c']
e -> d: ['e', 'E', 'D', 'd']
e -> e: ['e', 'E', 'e']
e -> f: ['e', 'E', 'F', 'f']
f -> a: ['f', 'F', 'E', 'A', 'a']
f -> b: ['f', 'F', 'E', 'B', 'b']
f -> c: ['f', 'F', 'E', 'B', 'C', 'c']
f -> d: ['f', 'F', 'E', 'D', 'd']
f -> e: ['f', 'F', 'E', 'e']
f -> f: ['f', 'F', 'f']

SUCCESS: All Routes correct!

## TESTS PASSED: 4/6

# Testing Distance Vector routing implementation

## 1. Testing /home/kineNg/Documents/ComputerNetwork/routing/06_pg242_net_events.json with DVrouter

a -> a: ['a', 'A', 'a']
a -> b: ['a', 'A', 'E', 'B', 'b']
a -> c: [] Incorrect Route
a -> d: [] Incorrect Route
a -> e: ['a', 'A', 'E', 'e']
a -> f: ['a', 'A', 'E', 'F', 'f']
b -> a: ['b', 'B', 'E', 'A', 'a']
b -> b: ['b', 'B', 'b']
b -> c: [] Incorrect Route
b -> d: ['b', 'B', 'E', 'D', 'd']
b -> e: ['b', 'B', 'E', 'e']
b -> f: ['b', 'B', 'E', 'F', 'f']
c -> a: ['c', 'C', 'B', 'E', 'A', 'a']
c -> b: ['c', 'C', 'B', 'b']
c -> c: ['c', 'C', 'c']
c -> d: [] Incorrect Route
c -> e: ['c', 'C', 'B', 'E', 'e']
c -> f: ['c', 'C', 'B', 'E', 'F', 'f']
d -> a: [] Incorrect Route
d -> b: ['d', 'D', 'E', 'B', 'b']
d -> c: [] Incorrect Route
d -> d: ['d', 'D', 'd']
d -> e: ['d', 'D', 'E', 'e']
d -> f: ['d', 'D', 'E', 'F', 'f']
e -> a: ['e', 'E', 'A', 'a']
e -> b: ['e', 'E', 'B', 'b']
e -> c: [] Incorrect Route
e -> d: ['e', 'E', 'D', 'd']
e -> e: ['e', 'E', 'e']
e -> f: ['e', 'E', 'F', 'f']
f -> a: ['f', 'F', 'E', 'A', 'a']
f -> b: ['f', 'F', 'E', 'B', 'b']
f -> c: [] Incorrect Route
f -> d: ['f', 'F', 'E', 'D', 'd']
f -> e: ['f', 'F', 'E', 'e']
f -> f: ['f', 'F', 'f']

FAILURE: Not all routes are correct

---

## 2. Testing /home/kineNg/Documents/ComputerNetwork/routing/03_pg244_net.json with DVrouter

a -> a: ['a', 'A', 'a']
a -> b: ['a', 'A', 'B', 'b']
a -> c: ['a', 'A', 'C', 'c']
a -> d: ['a', 'A', 'C', 'D', 'd']
a -> e: ['a', 'A', 'E', 'e']
a -> f: ['a', 'A', 'F', 'f']
a -> g: ['a', 'A', 'F', 'G', 'g']
b -> a: ['b', 'B', 'A', 'a']
b -> b: ['b', 'B', 'b']
b -> c: ['b', 'B', 'C', 'c']
b -> d: ['b', 'B', 'C', 'D', 'd']
b -> e: ['b', 'B', 'A', 'E', 'e']
b -> f: ['b', 'B', 'A', 'F', 'f']
b -> g: ['b', 'B', 'C', 'D', 'G', 'g']
c -> a: ['c', 'C', 'A', 'a']
c -> b: ['c', 'C', 'B', 'b']
c -> c: ['c', 'C', 'c']
c -> d: ['c', 'C', 'D', 'd']
c -> e: ['c', 'C', 'A', 'E', 'e']
c -> f: ['c', 'C', 'A', 'F', 'f']
c -> g: ['c', 'C', 'D', 'G', 'g']
d -> a: ['d', 'D', 'C', 'A', 'a']
d -> b: ['d', 'D', 'C', 'B', 'b']
d -> c: ['d', 'D', 'C', 'c']
d -> d: ['d', 'D', 'd']
d -> e: ['d', 'D', 'C', 'A', 'E', 'e']
d -> f: ['d', 'D', 'G', 'F', 'f']
d -> g: ['d', 'D', 'G', 'g']
e -> a: ['e', 'E', 'A', 'a']
e -> b: ['e', 'E', 'A', 'B', 'b']
e -> c: ['e', 'E', 'A', 'C', 'c']
e -> d: ['e', 'E', 'A', 'C', 'D', 'd']
e -> e: ['e', 'E', 'e']
e -> f: ['e', 'E', 'A', 'F', 'f']
e -> g: ['e', 'E', 'A', 'F', 'G', 'g']
f -> a: ['f', 'F', 'A', 'a']
f -> b: ['f', 'F', 'A', 'B', 'b']
f -> c: ['f', 'F', 'A', 'C', 'c']
f -> d: ['f', 'F', 'G', 'D', 'd']
f -> e: ['f', 'F', 'A', 'E', 'e']
f -> f: ['f', 'F', 'f']
f -> g: ['f', 'F', 'G', 'g']
g -> a: ['g', 'G', 'F', 'A', 'a']
g -> b: ['g', 'G', 'D', 'C', 'B', 'b']
g -> c: ['g', 'G', 'D', 'C', 'c']
g -> d: ['g', 'G', 'D', 'd']
g -> e: ['g', 'G', 'F', 'A', 'E', 'e']
g -> f: ['g', 'G', 'F', 'f']
g -> g: ['g', 'G', 'g']

SUCCESS: All Routes correct!

---

## 3. Testing /home/kineNg/Documents/ComputerNetwork/routing/01_small_net.json with DVrouter

b -> b: ['b', 'A', 'b']
b -> c: ['b', 'A', 'c']
b -> d: ['b', 'A', 'E', 'd']
c -> b: ['c', 'A', 'b']
c -> c: ['c', 'A', 'c']
c -> d: ['c', 'A', 'E', 'd']
d -> b: ['d', 'E', 'A', 'b']
d -> c: ['d', 'E', 'A', 'c']
d -> d: ['d', 'E', 'd']

SUCCESS: All Routes correct!

---

## 4. Testing /home/kineNg/Documents/ComputerNetwork/routing/04_pg244_net_events.json with DVrouter

a -> a: ['a', 'A', 'a']
a -> b: ['a', 'A', 'B', 'b']
a -> c: ['a', 'A', 'C', 'c']
a -> d: ['a', 'A', 'C', 'D', 'd']
a -> e: ['a', 'A', 'E', 'e']
a -> f: ['a', 'A', 'F', 'f']
a -> g: [] Incorrect Route
b -> a: ['b', 'B', 'A', 'a']
b -> b: ['b', 'B', 'b']
b -> c: ['b', 'B', 'C', 'c']
b -> d: ['b', 'B', 'C', 'D', 'd']
b -> e: ['b', 'B', 'A', 'E', 'e']
b -> f: ['b', 'B', 'A', 'F', 'f']
b -> g: [] Incorrect Route
c -> a: ['c', 'C', 'A', 'a']
c -> b: ['c', 'C', 'B', 'b']
c -> c: ['c', 'C', 'c']
c -> d: ['c', 'C', 'D', 'd']
c -> e: ['c', 'C', 'A', 'E', 'e']
c -> f: ['c', 'C', 'A', 'F', 'f']
c -> g: ['c', 'C', 'D', 'G', 'g']
d -> a: ['d', 'D', 'C', 'A', 'a']
d -> b: ['d', 'D', 'C', 'B', 'b']
d -> c: ['d', 'D', 'C', 'c']
d -> d: ['d', 'D', 'd']
d -> e: [] Incorrect Route
d -> f: ['d', 'D', 'G', 'F', 'f']
d -> g: ['d', 'D', 'G', 'g']
e -> a: ['e', 'E', 'A', 'a']
e -> b: ['e', 'E', 'A', 'B', 'b']
e -> c: ['e', 'E', 'A', 'C', 'c']
e -> d: ['e', 'E', 'A', 'C', 'D', 'd']
e -> e: ['e', 'E', 'e']
e -> f: ['e', 'E', 'A', 'F', 'f']
e -> g: [] Incorrect Route
f -> a: ['f', 'F', 'A', 'a']
f -> b: ['f', 'F', 'A', 'B', 'b']
f -> c: ['f', 'F', 'A', 'C', 'c']
f -> d: ['f', 'F', 'G', 'D', 'd']
f -> e: ['f', 'F', 'A', 'E', 'e']
f -> f: ['f', 'F', 'f']
f -> g: ['f', 'F', 'G', 'g']
g -> a: [] Incorrect Route
g -> b: [] Incorrect Route
g -> c: ['g', 'G', 'D', 'C', 'c']
g -> d: ['g', 'G', 'D', 'd']
g -> e: [] Incorrect Route
g -> f: ['g', 'G', 'F', 'f']
g -> g: ['g', 'G', 'g']

FAILURE: Not all routes are correct

---

## 5. Testing /home/kineNg/Documents/ComputerNetwork/routing/02_small_net_events.json with DVrouter

b -> b: ['b', 'A', 'b']
b -> c: ['b', 'A', 'c']
b -> d: [] Incorrect Route
c -> b: ['c', 'A', 'b']
c -> c: ['c', 'A', 'c']
c -> d: [] Incorrect Route
d -> b: [] Incorrect Route
d -> c: [] Incorrect Route
d -> d: ['d', 'E', 'd']

FAILURE: Not all routes are correct

---

## 6. Testing /home/kineNg/Documents/ComputerNetwork/routing/05_pg242_net.json with DVrouter

a -> a: ['a', 'A', 'a']
a -> b: ['a', 'A', 'E', 'B', 'b']
a -> c: ['a', 'A', 'E', 'B', 'C', 'c']
a -> d: ['a', 'A', 'E', 'D', 'd']
a -> e: ['a', 'A', 'E', 'e']
a -> f: ['a', 'A', 'E', 'F', 'f']
b -> a: ['b', 'B', 'E', 'A', 'a']
b -> b: ['b', 'B', 'b']
b -> c: ['b', 'B', 'C', 'c']
b -> d: ['b', 'B', 'E', 'D', 'd']
b -> e: ['b', 'B', 'E', 'e']
b -> f: ['b', 'B', 'E', 'F', 'f']
c -> a: ['c', 'C', 'B', 'E', 'A', 'a']
c -> b: ['c', 'C', 'B', 'b']
c -> c: ['c', 'C', 'c']
c -> d: ['c', 'C', 'B', 'E', 'D', 'd']
c -> e: ['c', 'C', 'B', 'E', 'e']
c -> f: ['c', 'C', 'B', 'E', 'F', 'f']
d -> a: ['d', 'D', 'E', 'A', 'a']
d -> b: ['d', 'D', 'E', 'B', 'b']
d -> c: ['d', 'D', 'E', 'B', 'C', 'c']
d -> d: ['d', 'D', 'd']
d -> e: ['d', 'D', 'E', 'e']
d -> f: ['d', 'D', 'E', 'F', 'f']
e -> a: ['e', 'E', 'A', 'a']
e -> b: ['e', 'E', 'B', 'b']
e -> c: ['e', 'E', 'B', 'C', 'c']
e -> d: ['e', 'E', 'D', 'd']
e -> e: ['e', 'E', 'e']
e -> f: ['e', 'E', 'F', 'f']
f -> a: ['f', 'F', 'E', 'A', 'a']
f -> b: ['f', 'F', 'E', 'B', 'b']
f -> c: ['f', 'F', 'E', 'B', 'C', 'c']
f -> d: ['f', 'F', 'E', 'D', 'd']
f -> e: ['f', 'F', 'E', 'e']
f -> f: ['f', 'F', 'f']

SUCCESS: All Routes correct!

## TESTS PASSED: 3/6
