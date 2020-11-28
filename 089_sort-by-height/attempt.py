def sort_by_height(heights):
    result = [-1] * len(heights)
    temp = []
    for i in range(len(heights)):
        if (heights[i] != -1):
            temp.append(heights[i])

    temp.sort()

    index = 0
    for j in range(len(heights)):
        if (heights[j] != -1):
            result[j] = temp[index]
            index += 1

    return result


# Test
print(sort_by_height([-1, 150, 190, 170, -1, -1, 160, 180]))
# [-1, 150, 160, 170, -1, -1, 180, 190]
