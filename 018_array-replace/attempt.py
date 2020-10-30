def array_place(array, to_replace, elem):
    for i in range(len(array)):
        if (array[i] == to_replace):
            array[i] = elem
    return array


# Test
print(array_place([1, 2, 1], 1, 3))  # [3, 2, 3]
print(array_place([1, 1, 1], 1, 3))  # [3, 3, 3]
print(array_place([2, 2, 2], 2, 1))  # [1, 1, 1]
