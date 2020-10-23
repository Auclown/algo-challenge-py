def add_two_digits(num):
    num_string = str(num)
    return int(num_string[0]) + int(num_string[1])


# Test
print(add_two_digits(29))  # 11
