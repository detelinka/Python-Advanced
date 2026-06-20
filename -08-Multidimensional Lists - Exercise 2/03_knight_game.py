n = int(input())
board = []

for _ in range(n):
    board.append(list(input()))

knight_moves = [
    (-2, -1), (-2, 1),
    (-1, -2), (-1, 2),
    (1, -2), (1, 2),
    (2, -1), (2, 1)
]

removed_knights = 0

while True:
    max_attack = 0
    knight_to_remove = None

    for row in range(n):
        for col in range(n):
            if board[row][col] == "K":
                attack = 0
                for move_row, move_col in knight_moves:
                    next_row = row + move_row
                    next_col = col + move_col

                    if 0 <= next_row < n and 0 <= next_col < n:
                        if board[next_row][next_col] == "K":
                            attack += 1
                if attack > max_attack:
                    max_attack = attack
                    knight_to_remove = [row, col]

    if max_attack == 0:
        break

    row, col = knight_to_remove
    board[row][col] = "0"
    removed_knights += 1

print(removed_knights)
