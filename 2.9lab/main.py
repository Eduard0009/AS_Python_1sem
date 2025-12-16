def process_matrix_files(file1, file2, m, n):
    def read_matrices(filename):
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
        matrices = []
        for i in range(0, len(lines), m):
            matrix = []
            for j in range(m):
                row = list(map(float, lines[i + j].split()))
                matrix.append(row)
            matrices.append(matrix)
        return matrices

    def write_matrices(filename, matrices):
        with open(filename, 'w') as f:
            for matrix in matrices:
                for row in matrix:
                    f.write(' '.join(map(str, row)) + '\n')

    matrices1 = read_matrices(file1)
    matrices2 = read_matrices(file2)

    for mat in matrices1:
        if mat not in matrices2:
            matrices2.append(mat)

    write_matrices(file2, matrices2)

    print("Содержимое первого файла:")
    with open(file1, 'r') as f:
        print(f.read())

    print("Содержимое второго файла:")
    with open(file2, 'r') as f:
        print(f.read())
