def Transp(A, M):
    B = [[0] * M for _ in range(M)]
    
    for i in range(M):
        for j in range(M):
            B[j][i] = A[i][j]
    
    return B


M = int(input("Введите порядок матрицы M: "))

A = []
print("Введите элементы матрицы:")
for i in range(M):
    row = list(map(float, input().split()))
    A.append(row)

B = Transp(A, M)

print("Транспонированная матрица:")
for row in B:
    print(*row)
