n = int(input())

odd_set = set()
even_set = set()

for row in range(1, n + 1):
    name = input()
    ascii_sum = sum(ord(ch) for ch in name)
    value = ascii_sum // row

    if value % 2 == 0:
        even_set.add(value)
    else:
        odd_set.add(value)

sum_odd = sum(odd_set)
sum_even = sum(even_set)

if sum_odd == sum_even: result = odd_set | even_set
elif sum_odd > sum_even: result = odd_set - even_set
else: result = odd_set ^ even_set

print(", ".join(str(x) for x in result))
