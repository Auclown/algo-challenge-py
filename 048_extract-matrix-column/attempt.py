def extract_matrix_col(matrix, col):
    result = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == col:
                result.append(matrix[i][j])

    return result


# Test
print(extract_matrix_col([[1, 1, 1, 2],
                          [0, 5, 0, 4],
                          [2, 1, 3, 6]], 2))
# [1, 0, 3]
