rows, cols = map(int, input().split())
matrix = []
for _ in range(rows):
    matrix.append(list(map(int, input().split())))

max_sum = float('-inf')
best_r = 0
best_c = 0

for r in range(rows - 2):
    for c in range(cols - 2):
        current_sum = sum(matrix[r + i][c + j] for i in range(3) for j in range(3))
        if current_sum > max_sum:
            max_sum = current_sum
            best_r = r
            best_c = c

print(f"Sum = {max_sum}")
for i in range(3):
    print(' '.join(str(matrix[best_r + i][best_c + j]) for j in range(3)))
