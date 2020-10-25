def almost_increasing_sequence(array):
    count = 0

    for i in range(len(array) - 1):
        if (array[i] <= array[i - 1]):
            count += 1
            if ((array[i] <= array[i - 2]) and (array[i + 1] <= array[i - 1])):
                return False

    return count <= 1


# Test
print(almost_increasing_sequence([1, 3, 2, 1]))  # False
print(almost_increasing_sequence([1, 3, 2]))  # True
