n = int(input())

matrix = []

for _ in range(n):
    data = list(input())
    matrix.append(data)

symbol = input()
position = None

for row in range(n):
    for column in range(n):
        if symbol == matrix[row][column] == symbol:
            position = (row, column)
            print(position)
            exit()

print(f"{symbol} does not occur in the matrix")