def closest_pair(nums, _sum):
    result = -1

    for i in range(len(nums)):
        for j in range(i + 1, len(nums) - 1):
            current = abs(i - j)

            if (nums[i] + nums[j] == _sum):
                if (result == -1 or current < result):
                    result = current

    return result


# Test
print(closest_pair([1, 0, 2, 4, 3, 0], 5))  # 2
print(closest_pair([2, 3, 7], 8))  # -1
