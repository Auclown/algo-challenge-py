def switch_lights(a):
    for i in range(1, len(a)):
        if (a[i] == 1):
            for j in range(i):
                a[j] = 0 if a[j] == 1 else 1

    return a


# Test
print(switch_lights([1, 1, 1, 1, 1]))  # [0, 1, 0, 1, 0]
print(switch_lights([0, 0]))  # [0, 0]
