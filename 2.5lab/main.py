def C(m, n):
    global call_count
    call_count += 1

    if m == 0 or m == n:
        return 1
    else:
        return C(m, n - 1) + C(m - 1, n - 1)


N = int(input("Введите число N: "))

M_values = []
print("Введите 5 различных значений M:")
for i in range(5):
    M = int(input())
    M_values.append(M)

for M in M_values:
    call_count = 0
    result = C(M, N)
    print("C(", M, ",", N, ") =", result, 
          "Количество рекурсивных вызовов:", call_count)
