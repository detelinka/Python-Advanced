rows, cols = map(int, input().split())
snake = input()

for r in range(rows):
    row_chars = []
    for c in range(cols):
        index = (r * cols + c) % len(snake)
        row_chars.append(snake[index])
    if r % 2 == 1:
        row_chars.reverse()
    print(''.join(row_chars))
