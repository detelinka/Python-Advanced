stack = []

n = int(input())

for _ in range(n):
    command = input().split()

    if command[0] == "1":
        number = int(command[1])
        stack.append(number)
    elif command[0] == "2":
        if stack:
            stack.pop()
    elif command[0] == "3":
        print(max(stack))
    elif command[0] == "4":
        print(min(stack))

print(", ".join(str(x) for x in reversed(stack)))
