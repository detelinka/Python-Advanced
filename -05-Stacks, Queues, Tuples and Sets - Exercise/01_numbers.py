nums_1 = set(map(int, input().split()))
nums_2 = set(map(int, input().split()))

for _ in range(int(input())):
    command = input()
    parts = command.split()

    if command.startswith("Add First"):
        for x in parts[2:]:
            nums_1.add(int(x))
    elif command.startswith("Add Second"):
        for x in parts[2:]:
            nums_2.add(int(x))
    elif command.startswith("Remove First"):
        for x in parts[2:]:
            nums_1.discard(int(x))
    elif command.startswith("Remove Second"):
        for x in parts[2:]:
            nums_2.discard(int(x))
    elif command.startswith("Check Subset"):
        print(nums_1.issubset(nums_2) or nums_2.issubset(nums_1))

print(", ".join(map(str, sorted(nums_1))))
print(", ".join(map(str, sorted(nums_2))))
