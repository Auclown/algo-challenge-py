def matrix_element_sum(matrix):
    result = 0
    zero_indices = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j] == 0):
                zero_indices.append(j)
            elif (not j in zero_indices):
                result += matrix[i][j]

    return result


# Test
print(matrix_element_sum([[0, 1, 1, 2],
                          [0, 5, 0, 0],
                          [2, 0, 3, 3]]))
# 9
