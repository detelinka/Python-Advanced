substrings = input().split()
valid_colors = {"red", "yellow", "blue", "orange", "purple", "green"}
found_colors = []

while substrings:
    if len(substrings) == 1:
        if substrings[0] in valid_colors:
            found_colors.append(substrings[0])
        break

    first = substrings.pop(0)
    last = substrings.pop()

    combo1 = first + last
    combo2 = last + first

    if combo1 in valid_colors:
        found_colors.append(combo1)
    elif combo2 in valid_colors:
        found_colors.append(combo2)
    else:
        first_trimmed = first[:-1]
        last_trimmed = last[:-1]
        mid = len(substrings) // 2
        if last_trimmed:
            substrings.insert(mid, last_trimmed)
        if first_trimmed:
            substrings.insert(mid, first_trimmed)

main_found = {c for c in found_colors if c in {"red", "yellow", "blue"}}
result = []
for color in found_colors:
    if color == "orange" and not {"red", "yellow"}.issubset(main_found):
        continue
    if color == "purple" and not {"red", "blue"}.issubset(main_found):
        continue
    if color == "green" and not {"yellow", "blue"}.issubset(main_found):
        continue
    result.append(color)

print(result)
