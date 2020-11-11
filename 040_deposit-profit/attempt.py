def deposit_profit(deposit, rate, threshold):
    year = 0

    while (deposit < threshold):
        deposit += deposit * (rate / 100)
        year += 1

    return year


# Test
print(deposit_profit(100, 20, 170))  # 3
