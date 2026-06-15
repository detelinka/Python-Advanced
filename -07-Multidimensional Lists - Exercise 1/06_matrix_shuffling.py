rows, cols = map(int, input().split())
matrix = []
for _ in range(rows):
    matrix.append(input().split())

while True:
    command = input()
    if command == "END":
        break

    parts = command.split()

    if len(parts) != 5 or parts[0] != "swap":
        print("Invalid input!")
        continue

    try:
        r1, c1, r2, c2 = int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4])
    except ValueError:
        print("Invalid input!")
        continue

    if r1 < 0 or r1 >= rows or c1 < 0 or c1 >= cols or r2 < 0 or r2 >= rows or c2 < 0 or c2 >= cols:
        print("Invalid input!")
        continue

    matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]

    for row in matrix:
        print(' '.join(row))
