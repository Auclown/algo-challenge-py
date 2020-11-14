import math


def fermactor(n):
    for i in range(n):
        for j in range(i):
            temp = math.pow(i, 2) - math.pow(j, 2)
            if (temp == n):
                return [i, j]


# Test
print(fermactor(15))  # [4, 1]
