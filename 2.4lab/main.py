# а) Функция calculate
def calculate(a, b, operation='add'):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return a / b
    else:
        return None


# б) Функция modify_strings
def modify_strings(strings, case=None):
    if case == 'upper':
        return [s.upper() for s in strings]
    elif case == 'lower':
        return [s.lower() for s in strings]
    else:
        return strings


# в) Функция average
def average(*numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


# Примеры использования функций
print(calculate(10, 5))                          # 15
print(calculate(10, 5, operation='multiply'))    # 50

print(modify_strings(['Hello', 'World']))                 # ['Hello', 'World']
print(modify_strings(['Hello', 'World'], case='upper'))  # ['HELLO', 'WORLD']

print(average(1, 2, 3, 4, 5))  # 3.0
print(average(10, 20))         # 15.0
