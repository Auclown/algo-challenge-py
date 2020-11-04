def chunky_monkey(array, size):
    first_half = []
    secnd_half = []

    for i in range(len(array)):
        if (i < size):
            first_half.append(array[i])
        else:
            secnd_half.append(array[i])

    return [first_half, secnd_half]


# Test
print(chunky_monkey(["a", "b", "c", "d"], 2))  # ["a", "b"], ["c", "d"]
print(chunky_monkey([0, 1, 2, 3, 4, 5], 4))  # [[0, 1, 2, 3], [4, 5]]
