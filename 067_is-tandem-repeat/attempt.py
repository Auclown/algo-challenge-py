def is_repeat(inp_string):
    length = len(inp_string)
    mid_point = int(length / 2)

    if (length % 2 == 0):
        first_half = inp_string[:mid_point]
        second_half = inp_string[mid_point:]

        return first_half == second_half

    return False


# Test
print(is_repeat("tandemtandem"))  # True
print(is_repeat("qqq"))  # False
print(is_repeat("2w2ww"))  # False
