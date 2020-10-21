import math


def absolute_value_sum_minimization(a):
    result = 0

    if (len(a) % 2 == 0):
        result = a[int(len(a) / 2 - 1)]
    else:
        index = math.floor(len(a) / 2)
        result = a[index]

    print(result)
    return result


# Test
absolute_value_sum_minimization([2, 4, 7])  # 4
absolute_value_sum_minimization([2, 4, 7, 6])  # 4
absolute_value_sum_minimization([2, 4, 7, 6, 6])  # 7
absolute_value_sum_minimization([2, 4, 7, 6, 6, 8])  # 7
