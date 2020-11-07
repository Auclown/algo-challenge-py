def compare_integers(a, b):
    a = int(a)
    b = int(b)

    if a < b:
        print("less")

    if a > b:
        print("greater")

    if a == b:
        print("equal")


# Test
compare_integers("12", "13")  # less
compare_integers("875", "799")  # greater
compare_integers("1000", "1000")  # equal
