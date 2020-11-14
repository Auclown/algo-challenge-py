def fancy_ride(l, fares):
    balance = 20
    options = ["UberX", "UberXL", "UberPlus", "UberBlack", "UberSUV"]

    for i in range(len(fares) - 1, 0, -1):
        if (fares[i] * l <= balance):
            return options[i]


# Test
print(fancy_ride(30, [0.3, 0.5, 0.7, 1, 1.3]))  # UberXL
