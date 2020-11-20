def largest_of_four(lists):
    return [max(i) for i in lists]


# Test
print(largest_of_four([[4, 5, 1, 3], [13, 27, 18, 26],
                       [32, 35, 37, 39], [1000, 1001, 857, 1]]))
# [5, 27, 39, 1001]
print(largest_of_four([[4, 9, 1, 3], [13, 35, 18, 26],
                       [32, 35, 97, 39], [1000000, 1001, 857, 1]]))
# [9, 35, 97, 1000000]
