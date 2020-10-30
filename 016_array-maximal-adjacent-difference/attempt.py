def amad(array):
    cur_max = 0

    for i in range(len(array) - 1):
        diff = abs(array[i]) - abs(array[i + 1])
        if (diff > cur_max):
            cur_max = diff

    return cur_max


# Test
print(amad([2, 4, 1, 0]))  # 3
print(amad([2, 9, 1, 0]))  # 8
