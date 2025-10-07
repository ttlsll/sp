def multiply_matrices(A, B):

    if len(A[0]) != len(B):
        raise ValueError("Матрицы несовместимы для умножения")

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]

print(multiply_matrices(A, B))

