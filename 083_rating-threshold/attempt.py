def rating_threshold(threshold, ratings):
    result = []

    for i in range(len(ratings)):
        if (sum(ratings[i]) / len(ratings[i]) < threshold):
            result.append(i)

    return result


# Test
print(rating_threshold(3.5, [[3, 4],
                             [3, 3, 3, 4],
                             [4]]))
# [1]
