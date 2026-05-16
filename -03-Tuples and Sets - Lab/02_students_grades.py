n = int(input())
students = {}
for i in range(n):
    name, grade = input().split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for name, grades in students.items():
    print(f"{name} -> {' '.join([f'{el:.2f}' for el in grades])} (avg: {sum(grades) / len(grades):.2f})")