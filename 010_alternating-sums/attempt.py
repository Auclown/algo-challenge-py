def alternating_sums(people):
    team_one = 0
    team_two = 0
    for i in range(len(people)):
        if i % 2 == 0:
            team_one += people[i]
        else:
            team_two += people[i]

    return [team_one, team_two]


# Test
print(alternating_sums([50, 60, 60, 45, 70]))  # [180, 105]
