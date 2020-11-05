def circle_of_numbers(n, first_number):
    numbers = []
    half = int(n / 2)

    for i in range(n):
        numbers.append(i)

    if (first_number < half):
        return numbers[first_number + half]

    return numbers[first_number - half]


# Test
print(circle_of_numbers(10, 2))  # 7
