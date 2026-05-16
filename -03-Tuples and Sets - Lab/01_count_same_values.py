numbers = tuple([float(el) for el in input().split()])

data = {}

for el in numbers:
    if el not in data:
        data[el] = numbers.count(el)

for key, value in data.items():
    print(f"{key:.1f} - {value} times")