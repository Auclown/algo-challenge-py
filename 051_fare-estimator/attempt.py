def fare_estimator(ride_time, distance, cpmin, cpmile):
    # (Cost per minute) * (ride time) + (Cost per mile) * (ride distance)
    result = []

    for i in range(len(cpmin)):
        result.append(
            round((cpmin[i] * ride_time) + (cpmile[i] * distance), 2))

    return result


# Test
print(fare_estimator(30, 7, [0.2, 0.35, 0.4, 0.45], [1.1, 1.8, 2.3, 3.5]))
# [13.7, 23.1, 28.1, 38]
