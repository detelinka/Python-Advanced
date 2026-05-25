from collections import deque

expression = input().split()
nums = deque()

for el in expression:

    if el in "+-*/":
        result = nums.popleft()
        while nums:
            current = nums.popleft()
            if el == "+":
                result += current
            elif el == "-":
                result -= current
            elif el == "*":
                result *= current
            elif el == "/":
                result //= current
        nums.append(result)
    else:
        nums.append(int(el))

print(nums[0])