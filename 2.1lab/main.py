from itertools import permutations

def check_key_in_dict(dictionary, keys_list):
    return all(key in dictionary for key in keys_list)

def generate_permutations(dictionary, key):
    if key not in dictionary:
        raise KeyError
    value = dictionary[key]
    if not isinstance(value, str):
        raise ValueError
    return [''.join(p) for p in permutations(value)]

def replace_with_mean(dictionary):
    return {k: round(sum(v) / len(v), 1) for k, v in dictionary.items() if isinstance(v, list)}
