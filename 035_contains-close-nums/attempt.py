def contains_close_nums(nums, k):
    result = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if (i != j and nums[i] == nums[j]):
                result.append(i)

    return abs(result[1] - result[0]) <= k


print(contains_close_nums([0, 1, 2, 3, 5, 2], 3))  # True
print(contains_close_nums([0, 1, 2, 3, 5, 2], 2))  # False
