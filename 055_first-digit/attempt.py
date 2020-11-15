import re


def first_digit(s):
    pattern = r'\d+'
    return re.search(pattern, s).group()


# Test
print(first_digit("var_1\_\_Int"))  # 1
print(first_digit("q2q-q"))  # 2
print(first_digit("0ss"))  # 0
