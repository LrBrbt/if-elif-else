def arithmetic(first_number, operator, second_number ):
    if operator == '+':
        return first_number + second_number
    elif operator == '-':
        return first_number - second_number
    elif operator == '*':
        return first_number * second_number
    elif operator == '/':
        return first_number / second_number
    else:
        return "Unknow operator"

print(arithmetic(2, '+', 2))
print(arithmetic(4, '-', 1))
print(arithmetic(3, '*', 10))
print(arithmetic(12, '/', 4))
print(arithmetic(2, '%', 3))