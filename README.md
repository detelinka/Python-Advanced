
# Python-Advanced

### 1. Lists as Stacks and Queues
Elements in a **stack** are added/removed from the
top ("last in, first out") or **LIFO** order
```python
stack.append(item) - добавяне на елемент
stack.pop(item) - премахване на елемент
```
Elements in a **queue** are added/removed from the
top ("first in, first out") or **FIFO** order
```python
my_queue = collections.deque() - създаване на deque

създаване на deque чрез import
from collections import deque
my_queue = deque() 

stack.append(item) - добавяне на елемент
stack.popleft(item) - премахване на елемент
```
### 2. Tuples and Sets
Tuples are a read-only collections. But the objects, inside the tuples, are mutable

```python
a = (1, 2, 3) # tuple
b = 1, 2, 3   # tuple
c = (1, )     # tuple
d = (1)       # int

a.count() - returns the number of times a specified value occurs
numbers = (1, 2, 1, 3, 1)
numbers.count(1) # 3

a.index() - returns the index of a particular element
names = ("Peter", "George", "George")
names.index("George") # 1
```
**Tuple Unpacking**
**Allows to extract tuple elements and assign them to elements**
```python

data = (1, 2, 3)
x, y, z = data
print(x) # 1
print(y) # 2
print(z) # 3

```
**Sets** are an unordered collections of items.
Every element of a set is unique.
Sets are mutable, so we can add or remove elements from it
Sets can be used to perform mathematical set operations (union, intersection, symmetric difference, etc.) 
```python
s = {a, b, c} # type(s) -> set

a = set([1, 2, 3, 4])
b = set([3, 4, 5, 6])

a | b # a.union(b) -> {1, 2, 3, 4, 5, 6}
a & b # a.intersection(b) -> {3, 4}
a <= b # a.issubset(b) -> False
a >= b # a.issuperset(b) -> False
a - b # a.difference(b) -> {1, 2}
a ^ b # a.symmetric_difference(b) -> {1, 2, 5, 6}
```

### 3. Multidimensional Lists /матрици/
Multidimensional lists in Python are lists that contain other lists as their elements, creating a nested structure that can represent grids, matrices, or higher-dimensional data.

**2D list (list of lists): GRID:**
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access row 1, column 2
print(matrix[1][2])  # 6
# Edit the matrix
matrix[1][2] = 10    # 10
```
**3D list: CUBE**
```python
cube = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

print(cube[1][0][1])  # 6
```
**Creating them dynamically:**
```python
# each row is an independent list (list comprehension)
rows, cols = 3, 4
grid = [[0 for _ in range(cols)] for _ in range(rows)]
```

**Creating MD List with Zeros - Using loops**
```python
matrix = []
for i in range(3):
    matrix.append([])
    for j in range(2):
        matrix[i].append(0)
        
# [[0, 0], [0, 0], [0, 0]]
```
**Creating 3X3 Grid with Numbers**
```python
matrix = []
for i in range(3):
    matrix.append([])
    for j in range(1, 4):
        matrix[i].append(j)
    
# [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
```
**Creating a matrix with zeros (using Comprehensions)**
```python
matrix = [[0 for j in range(2)] for i in range(3)]
```
**Creating a matrix with numbers (using Comprehensions)**
```python
matrix = [[j for j in range(1, 4)] for i in range(3)]
```
**Flattening a matrix (using Comprehensions)**
```python
matrix = [[1, 2, 3], [4, 5, 6]]
flattened = [num for sublist in matrix for num in sublist]
# [1, 2, 3, 4, 5, 6]
```
### 4. Functions Advanced
```python

```

### 5. Error Handling
### 6. File Handling
### 7. Workshop
### 8. Modules
### 9. Exam Preparation
### 10. Algorithms Introduction
### 11. Final Exam