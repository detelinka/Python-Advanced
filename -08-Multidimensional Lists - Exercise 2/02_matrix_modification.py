rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

while True:
    line = input()
    if line == "END":
        break

    parts = line.split()
    command = parts[0]
    row = int(parts[1])
    col = int(parts[2])
    value = int(parts[3])

    if 0 <= row < rows and 0 <= col < len(matrix[row]):
        if command == "Add":
            matrix[row][col] += value
        elif command == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

for row in matrix:
    print(' '.join(map(str, row)))
