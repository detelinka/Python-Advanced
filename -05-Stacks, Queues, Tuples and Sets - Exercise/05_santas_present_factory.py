from collections import deque

materials = list(map(int, input().split()))
magic = deque(map(int, input().split()))

presents = {}

while materials and magic:
    mat = materials.pop()
    mag = magic.popleft()

    if mat == 0 or mag == 0:
        if mat != 0:
            materials.append(mat)
        if mag != 0:
            magic.appendleft(mag)
        continue

    product = mat * mag

    if product == 150:
        presents["Doll"] = presents.get("Doll", 0) + 1
    elif product == 250:
        presents["Wooden train"] = presents.get("Wooden train", 0) + 1
    elif product == 300:
        presents["Teddy bear"] = presents.get("Teddy bear", 0) + 1
    elif product == 400:
        presents["Bicycle"] = presents.get("Bicycle", 0) + 1
    elif product < 0:
        materials.append(mat + mag)
    else:
        materials.append(mat + 15)

pair1 = presents.get("Doll", 0) >= 1 and presents.get("Wooden train", 0) >= 1
pair2 = presents.get("Teddy bear", 0) >= 1 and presents.get("Bicycle", 0) >= 1

if pair1 or pair2:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, reversed(materials)))}")
if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

for name in sorted(presents):
    print(f"{name}: {presents[name]}")
