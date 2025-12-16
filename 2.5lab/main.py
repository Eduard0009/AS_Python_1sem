def FibRec(n):
    global call_count
    call_count += 1
    if n == 1 or n == 2:
        return 1
    return FibRec(n - 2) + FibRec(n - 1)

# 5 чисел
for num in [5, 7, 10, 12, 15]:
    call_count = 0
    result = FibRec(num)
    print(f"F({num}) = {result}, вызовов: {call_count}")
