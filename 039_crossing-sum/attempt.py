def crossing_sum(matrix, a, b):
    row = 0
    col = 0

    for i in range(len(matrix)):
        row += matrix[a][i]
        col += matrix[i][b]

    return row + col


# Test
print(crossing_sum([[1, 1, 1, 1],
                    [2, 2, 2, 2],
                    [3, 3, 3, 3]], 1, 3))  # 12
