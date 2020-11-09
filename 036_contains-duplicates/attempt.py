def contains_duplicates(a):
    a = sorted(a)
    for i in range(len(a) - 1):
        if (a[i] == a[i+1]):
            return True

    return False


# Test
print(contains_duplicates([1, 2, 3, 1]))  # True
print(contains_duplicates([3, 1]))  # False
