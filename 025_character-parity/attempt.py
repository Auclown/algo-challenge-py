def character_parity(symbol):
    try:
        symbol = int(symbol)
        if (symbol % 2 == 0):
            print("even")
        else:
            print("odd")
    except ValueError:
        print("not a digit")


# Test
character_parity("5")  # odd
character_parity("8")  # even
character_parity("q")  # not a digit
