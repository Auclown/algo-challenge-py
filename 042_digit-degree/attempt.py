def digit_degree(n, c=0):
    count = c
    n_split = list(str(n))
    temp = 0

    if (len(n_split) <= 1):
        return count

    for i in range(len(n_split)):
        temp += int(n_split[i])
    count += 1

    return digit_degree(temp, count)


# Test
print(digit_degree(5))  # 0
print(digit_degree(100))  # 1
print(digit_degree(91))  # 2
