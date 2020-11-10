def convert_string(s, t):
    word = ""
    t_index = 0

    for i in range(len(s)):
        if s[i] == t[t_index]:
            word += s[i]
            t_index += 1

            if word == t:
                return True

    return False


# Test
print(convert_string("ceoydefthf5iyg5h5yts", "codefights"))  # True
print(convert_string("addbyca", "abcd"))  # False
