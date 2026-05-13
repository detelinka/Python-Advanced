n = int(input())
pumps = []

for _ in range(n):
    amount, distance = map(int, input().split())
    pumps.append((amount, distance))

start_index = 0
fuel = 0

for i in range(n):
    amount, distance = pumps[i]
    fuel += amount - distance
    if fuel < 0:
        fuel = 0
        start_index = i + 1

print(start_index)