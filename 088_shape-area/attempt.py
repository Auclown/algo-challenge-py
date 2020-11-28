def shape_area(n):
    area = 1

    for i in range(1, n):
        area += 4 * i

    return area


# Test
print(shape_area(2))  # 5
print(shape_area(3))  # 13
