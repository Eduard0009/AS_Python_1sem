def calculate(a, b, operation='add'):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return a / b

def modify_strings(strings, case=None):
    if case == 'upper':
        return [s.upper() for s in strings]
    elif case == 'lower':
        return [s.lower() for s in strings]
    else:
        return strings

def average(*args):
    return sum(args) / len(args) if args else 0

