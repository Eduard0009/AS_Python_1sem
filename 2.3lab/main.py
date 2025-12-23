def Transp(A, M):
    result = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            result[j][i] = A[i][j]
    return result
