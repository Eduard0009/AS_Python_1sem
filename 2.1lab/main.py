
# a) 
def has_all_keys(mapping, required):
    missing = False
    for elem in required:
        if elem not in mapping:
            missing = True
            break
    return not missing


data_map = {1: 2, 3: 4}
required_keys = [1, 3]
print(has_all_keys(data_map, required_keys))


# б) 
def letter_permutations(storage, index):
    if index not in storage:
        return []

    chars = storage[index]
    combinations = []

    for a in range(len(chars)):
        for b in range(len(chars)):
            for c in range(len(chars)):
                if len({a, b, c}) == 3:
                    combinations.append(chars[a] + chars[b] + chars[c])

    return combinations


letters_dict = {1: "abc"}
print(letter_permutations(letters_dict, 1))


# в) 
def mean_values(source):
    result = {}

    for k, values in source.items():
        total = 0
        count = 0
        for v in values:
            total += v
            count += 1
        result[k] = round(total / count, 1)

    return result


nums = {1: [2, 3, 4], 3: [5, 6, 7], 5: [8, 9, 0]}
print(mean_values(nums))
