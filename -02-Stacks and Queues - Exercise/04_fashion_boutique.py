boxes_of_clothes = list(map(int, input().split()))
capacity = int(input())

racks = 1
current_load = 0

while boxes_of_clothes:
    cloth = boxes_of_clothes.pop()
    if current_load + cloth <= capacity:
        current_load += cloth
    else:
        racks += 1
        current_load = cloth

print(racks)