import math


def late_ride(n):
    result = 0
    hours = math.floor(n / 60)
    mins = n % 60

    hours_string = "0" + str(hours) if hours < 10 else str(hours)
    mins_string = "0" + str(mins) if mins < 10 else str(mins)

    time = hours_string + mins_string

    for i in range(len(time)):
        result += int(time[i])

    return result


# Test
print(late_ride(240))  # 4
print(late_ride(808))  # 14
