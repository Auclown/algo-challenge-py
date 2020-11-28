def seek_and_destroy(init, seek):
    result = []
    for i in range(len(init)):
        if not init[i] in seek:
            result.append(init[i])

    return result


# Test
print(seek_and_destroy([3, 5, 1, 2, 2], [2, 3, 5]))  # [1]
print(seek_and_destroy([1, 2, 3, 5, 1, 2, 3], [2, 3]))  # [1, 5, 1]
