def house_of_cats(legs):
    cat = 0
    human = 0

    if (legs == 2):
        return [1]

    for i in range(legs, 0, -1):
        if i % 2 == 0 and i != 0:
            human += 1

    for j in range(legs, 0, -1):
        if j % 4 == 0 and j != 0:
            cat += 1

    return [cat, human]


# Test
print(house_of_cats(6))  # [1, 3]
print(house_of_cats(2))  # [1]
