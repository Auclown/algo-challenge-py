def convert_cel_to_far(temp):
    return int(temp * (9/5)) + 32


# Test
print(convert_cel_to_far(-30))  # - 22
print(convert_cel_to_far(-10))  # 14
print(convert_cel_to_far(0))  # 32
