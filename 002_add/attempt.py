def add(n1, n2):
    return n1 + n2


def add_2(*nums):
    result = 0
    for num in nums:
        result += num

    return result


# Test
print(add(1, 2)) # 3
print(add_2(1, 2, 3, 4, 5)) # 15
