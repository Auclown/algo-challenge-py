import re


def digits_prefix(string):
    numbers = re.findall(r'\d+', string)

    return max(numbers)


# Test
print(digits_prefix("123aa1"))  # 123
