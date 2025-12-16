def find_sum_min_max(filename):
    with open(filename, 'r') as f:
        numbers = [float(line.strip()) for line in f if line.strip()]
    
    return min(numbers) + max(numbers)
