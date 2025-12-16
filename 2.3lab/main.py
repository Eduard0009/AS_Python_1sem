def Transp(A, M):
    for i in range(M):
        for j in range(i + 1, M):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    return A
