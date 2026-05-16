
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
a = set([1, 2, 3, 4])
b = set([3, 4, 5, 6])

a | b # a.union(b) -> {1, 2, 3, 4, 5, 6}
a & b # a.intersection(b) -> {3, 4}
a <= b # a.issubset(b) -> False
a >= b # a.issuperset(b) -> False
a - b # a.difference(b) -> {1, 2}
a ^ b # a.symmetric_difference(b) -> {1, 2, 5, 6}
```
```python

```
```python

```
### 3. Stacks, Queues,Tuples and Sets
### 4. Multidimensional Lists
### 5. Functions Advanced
### 6. Error Handling
### 7. File Handling
### 8. Workshop
### 9. Modules
### 10. Exam Preparation
### 11. Algorithms Introduction
### 12. Final Exam