# а) 
def calculate(num1, num2, operation='add'):
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 / num2
    else:
        result = 0
    return result


# б) 
def modify_strings(text_list, case=None):
    new_list = []

    if case == 'upper':
        for text in text_list:
            new_list.append(text.upper())
        return new_list

    elif case == 'lower':
        for text in text_list:
            new_list.append(text.lower())
        return new_list

    else:
        return text_list


# в) 
def average(*nums):
    total = 0
    count = 0
    for n in nums:
        total += n
        count += 1
    return total / count


# г) 
def merge_dictionaries(start_dict, **extra_dicts):
    result_dict = start_dict.copy()

    for name in extra_dicts:
        one_dict = extra_dicts[name]
        for key in one_dict:
            result_dict[key] = one_dict[key]

    return result_dict



print(calculate(10, 5))
print(calculate(10, 5, operation='multiply'))

print(modify_strings(['Hello', 'World']))
print(modify_strings(['Hello', 'World'], case='upper'))

print(average(1, 2, 3, 4, 5))
print(average(10, 20))

print(merge_dictionaries({'a': 1, 'b': 2}, dict1={'b': 3, 'c': 4}))
print(merge_dictionaries({'x': 5}, dict1={'y': 6}, dict2={'z': 7}))
