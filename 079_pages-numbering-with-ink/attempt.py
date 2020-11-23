def panuwi(current, num_digits):
    ink_usage = len(str(current))

    while (num_digits > ink_usage):
        num_digits -= ink_usage

        if (num_digits >= ink_usage):
            current += 1

    return current


# Test
print(panuwi(1, 5))  # 5
print(panuwi(21, 5))  # 22
print(panuwi(8, 4))  # 10
