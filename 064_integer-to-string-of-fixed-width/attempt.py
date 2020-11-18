def int_to_string(number, width):
    number = str(number)
    to_get = -1 * width
    str_part = number[to_get:]
    zer_part = ""

    if (len(number) < width):
        diff = abs(width - len(number))
        for _ in range(diff):
            zer_part += "0"

    return zer_part + str_part


# Test
print(int_to_string(1234, 2))  # 34
print(int_to_string(1234, 4))  # 1234
print(int_to_string(1234, 5))  # 01234
