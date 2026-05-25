n = int(input())

periodic_table = set()

for _ in range(n):
    for el in input().split():
        periodic_table.add(el)

print(*periodic_table, sep='\n')