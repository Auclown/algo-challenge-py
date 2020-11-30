def sum_of_two(a, b, v):
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] + b[j] == v:
                return True

    return False


# Test
print(sum_of_two([1, 2, 3], [10, 20, 30, 40], 42))  # True
