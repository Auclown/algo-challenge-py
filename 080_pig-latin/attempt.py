def pig_latin(inp_string):
    vowels = ["a", "e", "i", "o", "u"]

    if inp_string[0] in vowels:
        return inp_string + "way"

    for i in range(len(inp_string)):
        if (inp_string[i] in vowels):
            first = inp_string[i:]
            second = inp_string[:i]
            return first + second + "ay"


# Test
print(pig_latin("glove"))  # oveglay
print(pig_latin("eight"))  # eightway
