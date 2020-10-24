def adjacent_elements_product(numbers):
    largest = 0

    for i in range(len(numbers) - 1):
        if (numbers[i] * numbers[i + 1] > largest):
            largest = numbers[i] * numbers[i + 1]

    return largest


# Test
print(adjacent_elements_product([3, 6, -2, -5, 7, 3]))  # 21
print(adjacent_elements_product([0, 2, 4, 10, 1, 5]))  # 40
