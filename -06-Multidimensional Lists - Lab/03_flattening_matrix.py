n = int(input())

matrix = []

for _ in range(n):
    data = [int(el) for el in input().split(", ")]
    matrix.extend(data)

print(matrix)