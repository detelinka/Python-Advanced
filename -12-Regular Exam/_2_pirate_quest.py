n = int(input())
grid = []
ship_row, ship_col = 0, 0

for i in range(n):
    line = input()
    row = line.split() if ' ' in line else list(line)
    for j in range(len(row)):
        if row[j] == 'S':
            ship_row, ship_col = i, j
    grid.append(row)

treasures = sum(cell == '*' for row in grid for cell in row)
durability = 100
charm_used = False
first_move = True

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

end_reason = None

while True:
    command = input()

    if command == 'stop':
        end_reason = 'stop'
        break

    if first_move:
        grid[ship_row][ship_col] = '.'
        first_move = False

    dr, dc = directions[command]
    ship_row = (ship_row + dr) % n
    ship_col = (ship_col + dc) % n

    cell = grid[ship_row][ship_col]

    if cell == '*':
        treasures -= 1
        grid[ship_row][ship_col] = '.'
        if treasures == 0:
            end_reason = 'all_collected'
            break
    elif cell == 'C':
        grid[ship_row][ship_col] = '.'
        if not charm_used:
            charm_used = True
            durability = min(100, durability + 25)
    elif cell == 'M':
        durability -= 25
        grid[ship_row][ship_col] = '.'
        if durability <= 0:
            durability = 0
            end_reason = 'shipwreck'
            break

if end_reason == 'shipwreck':
    print(f"Shipwreck! Last known coordinates ({ship_row}, {ship_col})")
elif end_reason == 'all_collected':
    print("Yo-ho-ho! All treasure chests collected!")
else:
    print("Retreat! Some treasures remain unclaimed.")

print(f"Ship Durability: {durability}")

if treasures > 0:
    print(f"Unclaimed chests: {treasures}")

grid[ship_row][ship_col] = 'S'
for row in grid:
    print(''.join(row))
