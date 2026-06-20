from collections import deque

drones = [
    ("Sentinel-X", 100),
    ("Viper-MKII", 85),
    ("Aegis-7", 75),
    ("Striker-R", 65),
    ("Titan-Core", 55)
]

parts = list(map(int, input().split()))
cells = deque(map(int, input().split()))

built = set()
assembled = []

while parts and cells and len(built) < 5:
    while cells and cells[0] <= 0:
        cells.popleft()
    if not cells:
        break

    part = parts.pop()
    cell = cells.popleft()
    total = part + cell

    exact = None
    for name, power in drones:
        if power == total and name not in built:
            exact = name
            break

    if exact:
        built.add(exact)
        assembled.append(exact)
    else:
        best = None
        best_power = -1
        for name, power in drones:
            if power < total and name not in built and power > best_power:
                best = name
                best_power = power

        if best:
            built.add(best)
            assembled.append(best)
            new_cell = cell - 30
            if new_cell > 0:
                cells.append(new_cell)
        else:
            new_cell = cell - 1
            if new_cell > 0:
                cells.append(new_cell)

if len(built) == 5:
    print("Mission Accomplished! All Guardian Drones activated!")
else:
    print("Mission Failed! Some drones were not built.")

if assembled:
    print(f"Assembled Drones: {', '.join(assembled)}")

if parts:
    print(f"Mechanical Parts: {', '.join(str(p) for p in reversed(parts))}")

if cells:
    print(f"Power Cells: {', '.join(str(c) for c in cells)}")
