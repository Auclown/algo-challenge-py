def company_bot_strategy(training_data):
    trainers_num = 0
    total_time = 0

    for i in range(len(training_data)):
        if (training_data[i][1] == 1):
            trainers_num += 1
            total_time += training_data[i][0]

    return total_time / trainers_num


# Test
print(company_bot_strategy([[3, 1],
                            [6, 1],
                            [4, 1],
                            [5, 1]]))
# 4.5

print(company_bot_strategy([[4, 1],
                            [4, -1],
                            [0, 0],
                            [6, 1]]))

# 5.0
