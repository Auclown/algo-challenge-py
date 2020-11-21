def missing_letters(string):
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    chars = list(string)

    for i in range(len(chars)):
        if (alphabets[i] != chars[i]):
            return alphabets[i]

    return None


# Test
print(missing_letters("abce"))  # d
print(missing_letters("abcdefghjklmno"))  # i
print(missing_letters("abcdefghijklmnopqrstuvwxyz"))  # None
