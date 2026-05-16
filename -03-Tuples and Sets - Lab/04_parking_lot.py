n = int(input())
parking_lot = set()

for _ in range(n):
    command, number = input().split(", ")
    if command == 'IN':
        parking_lot.add(number)
    if command == 'OUT':
        parking_lot.remove(number)


if len(parking_lot) == 0:
    print("Parking Lot is Empty")
else:
    for car in parking_lot:
        print(car)