import math


def max_multiple(divisor, bound):
    # result = 0
    # current = 0
    # while (current < bound):
    #     if (current % divisor == 0):
    #         result = current
    #     current += 1

    # return result

    return math.floor(bound / divisor) * divisor


# Test
print(max_multiple(3, 10))  # 9
