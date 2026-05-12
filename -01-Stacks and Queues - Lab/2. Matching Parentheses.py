expression = input()
parentheses = []

for char in range(len(expression)):
    if expression[char] == "(":
        parentheses.append(char)
    elif expression[char] == ")":
        start_index = parentheses.pop()
        end_index = char + 1
        print(expression[start_index:end_index])