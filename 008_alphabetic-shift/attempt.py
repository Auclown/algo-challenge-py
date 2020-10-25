def alphabetic_shift(word):
    chars = [char for char in word]
    updated = []

    for char in chars:
        if (char == "z"):
            updated.append("a")
        else:
            code = ord(char) + 1
            updated.append(chr(code))

    return "".join(updated)


# Test
print(alphabetic_shift("crazy"))  # dsbaz
