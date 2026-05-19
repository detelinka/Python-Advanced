from collections import deque

cups = deque(map(int, input().split()))
bottles = list(map(int, input().split()))

wasted = 0

while cups and bottles:
    current_cup = cups[0]
    current_bottle = bottles.pop()

    if current_bottle >= current_cup:
        wasted += current_bottle - current_cup
        cups.popleft()
    else:
        cups[0] = current_cup - current_bottle

if not cups:
    # All cups filled → print remaining bottles from last to first
    print("Bottles:", *reversed(bottles))
else:
    # Bottles finished → print remaining cups from first to last
    print("Cups:", *cups)

print(f"Wasted litters of water: {wasted}")
