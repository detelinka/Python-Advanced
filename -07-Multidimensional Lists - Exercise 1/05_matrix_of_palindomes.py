r, c = map(int, input().split())

for row in range(r):
    outer = chr(ord('a') + row)
    palindromes = []
    for col in range(c):
        middle = chr(ord('a') + row + col)
        palindromes.append(outer + middle + outer)
    print(' '.join(palindromes))
