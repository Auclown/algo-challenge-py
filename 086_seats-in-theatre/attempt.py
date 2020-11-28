def seats_in_theatre(cols_num, rows_num, col, row):
    return (cols_num - col + 1) * (rows_num - row)


# Test
print(seats_in_theatre(16, 11, 5, 3))  # 96
