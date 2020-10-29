def amc(array, k):
    maximum = 0

    for i in range(len(array) - k + 1):
        temp = 0
        count = 0

        while (count < k):
            temp += array[i + count]
            if (temp > maximum):
                maximum = temp
            count += 1

    return maximum


# Test
print(amc([2, 3, 5, 1, 6], 2))  # 8
print(amc([2, 3, 5, 1, 6], 3))  # 12
