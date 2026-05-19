from collections import deque

price_per_bullet = int(input())
barrel_size = int(input())

bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))
intelligence_value = int(input())

bullets_fired = 0
current_barrel = barrel_size

while bullets and locks:
    bullet = bullets.pop()
    lock = locks[0]
    bullets_fired += 1
    current_barrel -= 1

    if bullet <= lock:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")

    if current_barrel == 0 and bullets:
        print("Reloading!")
        current_barrel = barrel_size

if not locks:
    bullets_left = len(bullets)
    money_earned = intelligence_value - bullets_fired * price_per_bullet
    print(f"{bullets_left} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")