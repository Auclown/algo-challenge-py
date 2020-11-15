def first_duplicate(array):
    elements = []
    for i in range(len(array)):
        if (not array[i] in elements):
            elements.append(array[i])
        else:
            return array[i]

    return -1


# Test
print(first_duplicate([2, 1, 3, 5, 3, 2]))  # 3
print(first_duplicate([2, 4, 3, 5, 1]))  # -1
