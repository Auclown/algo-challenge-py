def house_number_sum(input_array):
    _sum = 0
    for i in range(len(input_array)):
        if (input_array[i] != 0):
            _sum += input_array[i]
        else:
            return _sum


# Test
print(house_number_sum([5, 1, 2, 3, 0, 1, 5, 0, 2]))  # 11
