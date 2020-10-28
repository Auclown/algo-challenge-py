def array_conversion(a):
    is_even = True
    while (len(a) > 1):
        temp = []
        for i in range(0, len(a), 2):
            if (is_even):
                temp.append(a[i] + a[i + 1])
            else:
                temp.append(a[i] * a[i + 1])
        a = temp
        is_even = not is_even
    return a[0]


# Test
print(array_conversion([1, 2, 3, 4, 5, 6, 7, 8]))  # 186
