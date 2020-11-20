def is_lucky(n):
    first_half_sum = 0
    second_half_sum = 0

    midpoint = int(len(str(n)) / 2)
    first_half = str(n)[:midpoint]
    second_half = str(n)[midpoint:]

    for i in range(len(first_half)):
        first_half_sum += int(first_half[i])

    for j in range(len(second_half)):
        second_half_sum += int(second_half[j])

    return first_half_sum == second_half_sum


# Test
print(is_lucky(1230))  # True
print(is_lucky(239017))  # False
