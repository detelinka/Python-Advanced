from collections import deque

chocolates = [int(el) for el in input().split(", ")]
milks = deque(int(el) for el in input().split(", "))

milkshakes = 0

while milkshakes < 5 and (chocolates and milks):

    if chocolates[-1] <= 0 or milks[0] <= 0:

        if chocolates[-1] <= 0:
            chocolates.pop()
        if milks[0] <= 0:
            milks.popleft()

    elif chocolates[-1] == milks[0]:
        milkshakes += 1
        chocolates.pop()
        milks.popleft()
    else:
        milks.rotate(-1)
        chocolates[-1] -= 5


if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print("Chocolate: " + ", ".join(map(str, chocolates)))
else:
    print("Chocolate: empty")

if milks:
    print("Milk: " + ", ".join(map(str, milks)))
else:
    print("Milk: empty")