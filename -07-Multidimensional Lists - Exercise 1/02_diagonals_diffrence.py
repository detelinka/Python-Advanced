n = int(input())
matrix = []

for _ in range(n):
    row = [int(el) for el in input().split()]
    matrix.append(row)

primary_sum = 0
secondary_sum = 0

for i in range(n):
    primary_sum += matrix[i][i]
    secondary_sum += matrix[i][n - 1 - i]

print(abs(primary_sum - secondary_sum))
