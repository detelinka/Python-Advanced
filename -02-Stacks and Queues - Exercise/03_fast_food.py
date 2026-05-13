from collections import deque

food = int(input())
orders = deque(map(int, input().split()))

print(max(orders))

while orders and food >= orders[0]:
    if food >= orders[0]:
        food -= orders[0]
        orders.popleft()

if not orders:
    print("Orders complete")
else:
    print("Orders left:", *orders)