def launch_sequence(system_names, steps):
    sequence = {}

    for i in range(len(system_names)):
        sequence[system_names[i]] = []

    for j in range(len(steps)):
        sequence[system_names[j]].append(steps[j])

    for _, value in sequence.items():
        for i in range(len(value) - 1):
            if value[i] >= value[i + 1]:
                return False

    return True


# Test
print(launch_sequence(["stage_1", "stage_2", "dragon", "stage_1",
                       "stage_2", "dragon"], [1, 10, 11, 2, 12, 111]))
# True
print(launch_sequence(["stage_1", "stage_1",
                       "stage_2", "dragon"], [2, 1, 12, 111]))
# False
