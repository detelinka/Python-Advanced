n = int(input())
matrix = []

for _ in range(n):
    data = [int(el) for el in input().split()]
    matrix.append(data)

diagonal_sum = 0

for row in range(n):
    for column in range(n):
        if row == column:
            diagonal_sum += matrix[row][column]

# OR
# for index in range(n):
#     diagonal_sum += matrix[index][index]


print(diagonal_sum)