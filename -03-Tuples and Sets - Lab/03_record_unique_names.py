n = int(input())
students = set()
for _ in range(n):
    name = input()
    students.add(name)

print(*students, sep='\n')