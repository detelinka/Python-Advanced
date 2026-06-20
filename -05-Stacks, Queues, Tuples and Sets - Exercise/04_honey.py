from collections import deque

bees = deque(map(int, input().split()))
nectar = list(map(int, input().split()))
symbols = deque(input().split())

total_honey = 0

while bees and nectar:
    bee = bees.popleft()
    matched = False

    while nectar:
        n = nectar.pop()
        if n >= bee:
            symbol = symbols.popleft()
            if symbol == '+':
                total_honey += abs(bee + n)
            elif symbol == '-':
                total_honey += abs(bee - n)
            elif symbol == '*':
                total_honey += abs(bee * n)
            elif symbol == '/':
                if n != 0:
                    total_honey += abs(bee / n)
            matched = True
            break

    if not matched:
        bees.appendleft(bee)
        break

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")
