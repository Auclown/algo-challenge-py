def tasks_types(deadlines, day):
    today = 0
    upcoming = 0
    later = 0

    for i in range(len(deadlines)):
        if deadlines[i] <= day:
            today += 1
        elif abs(deadlines[i] - day) > 7:
            later += 1
        else:
            upcoming += 1

    return [today, upcoming, later]


# Test
print(tasks_types([1, 2, 3, 4, 5], 2))  # [2, 3, 0]
print(tasks_types([1, 2, 4, 2, 10, 3, 1, 4, 5, 4, 9, 8], 1))  # [2, 8, 2]
