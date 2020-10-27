def are_similar(a, b):
    if (a == b):
        return True

    difference = []
    to_compare = []

    for i in range(len(a)):
        if (a[i] != b[i]):
            difference.append(a[i])
            to_compare.append(b[i])

    to_compare = to_compare.reverse()

    if (len(difference) == 2 and (difference == to_compare)):
        return True

    return False


# Test
print(are_similar([1, 2, 3], [1, 2, 3]))  # True
print(are_similar([1, 2, 3], [2, 1, 3]))  # True
print(are_similar([1, 2, 2], [2, 1, 1]))  # False
