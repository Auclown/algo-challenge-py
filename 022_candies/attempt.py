import math


def candies(children, candies):
    each = math.floor(candies / children)

    return each * children


# Test
print(candies(3, 10))  # 9
