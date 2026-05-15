sequence = input().strip()

stack = []
pairs = {')': '(', ']': '[', '}': '{'}
is_balanced = True

for ch in sequence:
    if ch in '([{':
        stack.append(ch)
    elif ch in ')]}':
        if not stack or stack[-1] != pairs[ch]:
            is_balanced = False
            break
        stack.pop()

if is_balanced and not stack:
    print("YES")
else:
    print("NO")
