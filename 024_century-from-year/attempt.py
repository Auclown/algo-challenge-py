import math


def century_from_year(year):
    return math.ceil(year / 100)


# Test
print(century_from_year(1905))  # 20
print(century_from_year(1700))  # 17
print(century_from_year(1701))  # 18
print(century_from_year(2000))  # 20
