def cip(input_string):
    input_string = input_string.lower()
    reversed_str = input_string[::-1]

    return input_string == reversed_str


# Test
print(cip("AaBaa"))  # True
print(cip("abac"))  # False
