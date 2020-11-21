def mac(statues):
    result = 0
    statues = sorted(statues)
    
    for i in range(len(statues) - 1):
        if (statues[i + 1] - statues[i] != 1):
            result += (statues[i + 1] - statues[i] - 1)

    return result


# Test
print(mac([6, 2, 3, 8]))  # 3
