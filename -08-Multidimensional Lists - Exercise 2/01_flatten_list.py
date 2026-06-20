sublists = input().split("|")
result = []

for sublist in reversed(sublists):
    nums = sublist.split()

    for num in nums:
        result.append(int(num))

print(' '.join(map(str, result)))