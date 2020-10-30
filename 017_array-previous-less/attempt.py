def apl(items):
    result = [-1]
    for i in range(len(items) - 1):
        if (items[i] < items[i + 1]):
            result.append(items[i])
        else:
            result.append(-1)

    return result


# Test
print(apl([3, 5, 2, 4, 5]))  # [-1, 3, -1, 2, 4]
