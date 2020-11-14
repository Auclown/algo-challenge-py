def extract_each_kth(input_array, k):
    del input_array[k-1::k]

    return input_array


# Test
print(extract_each_kth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
# [1, 2, 4, 5, 7, 8, 10]
