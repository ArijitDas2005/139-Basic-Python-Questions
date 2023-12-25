# Q.Write a Python Program to Transpose a Matrix.


def transpose_matrix(matrixe):
    rows, cols = len(matrixe), len(matrixe[0])
    # Create an empty matrix to store the transposed data
    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrixe[i][j]
    return result


# Input matrix
matrix = [
 [1, 2, 3],
 [4, 5, 6]
]

# Transpose the matrix
transposed_matrix = transpose_matrix(matrix)

# Print the transposed matrix
for row in transposed_matrix:
    print(row)
