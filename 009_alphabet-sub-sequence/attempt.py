def alphabet_sub_sequence(word):
    for i in range(len(word) - 1):
        if (ord(word[i]) >= ord(word[i + 1])):
            return False

    return True


# Test
print(alphabet_sub_sequence("effg"))  # False
print(alphabet_sub_sequence("cdce"))  # False
print(alphabet_sub_sequence("ace"))  # True
print(alphabet_sub_sequence("bxz"))  # True
