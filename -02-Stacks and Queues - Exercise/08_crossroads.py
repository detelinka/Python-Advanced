from collections import deque

green_duration = int(input())
free_window = int(input())

cars = deque()
passed_cars = 0
crash_happened = False

while True:
    command = input()
    if command == "END":
        break

    if command != "green":
        cars.append(command)
        continue

    current_green = green_duration

    while cars and current_green > 0:
        car = cars.popleft()
        car_length = len(car)

        if car_length <= current_green:
            current_green -= car_length
            passed_cars += 1
        else:
            remaining = car_length - current_green
            if remaining <= free_window:
                passed_cars += 1
                break
            else:
                hit_index = current_green + free_window
                hit_char = car[hit_index]
                print("A crash happened!")
                print(f"{car} was hit at {hit_char}.")
                crash_happened = True
                break

    if crash_happened:
        break

if not crash_happened:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")