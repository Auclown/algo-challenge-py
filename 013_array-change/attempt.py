def array_change(a):
    count = 0
    for i in range(len(a) - 1):
        if (a[i] >= a[i + 1]):
            diff = a[i] + 1 - a[i + 1]
            a[i + 1] = a[i] + 1
            count += diff

    return count


print(array_change([1, 1, 1]))
