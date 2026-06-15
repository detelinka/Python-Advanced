rows, cols = [int(el) for el in input().split(", ")]
matrix = []
for _ in range(rows):
    data = [int(el) for el in input().split(", ")]
    matrix.append(data)

max = float("-inf")
sub_matrix = []

for row in range(rows-1):
    for col in range(cols-1):
        current = matrix[row][col]
        next_el = matrix[row][col+1]
        el_bellow = matrix[row+1][col]
        el_diagonal = matrix[row+1][col+1]

        sum_elements = current + next_el + el_bellow + el_diagonal
        if sum_elements > max:
            max = sum_elements
            sub_matrix = [
                [current, next_el],
                [el_bellow, el_diagonal]
            ]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max)