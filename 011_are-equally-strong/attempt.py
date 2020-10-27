def are_equally_strong(urLeft, urRight, frndsLeft, frndsRight):
    urs = [urLeft, urRight]
    frnds = [frndsLeft, frndsRight]
    return min(urs) == min(frnds) and max(urs) == max(frnds)


# Test
print(are_equally_strong(10, 15, 15, 10))  # True
print(are_equally_strong(15, 10, 15, 10))  # True
print(are_equally_strong(15, 10, 15, 9))  # False
