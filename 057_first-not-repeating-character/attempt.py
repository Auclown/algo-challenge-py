def first_not_repeating_char(s):
    for i in range(len(s)):
        repeat = False
        for j in range(len(s)):
            if (s[i] == s[j]) and i != j:
                repeat = True

        if not repeat:
            return s[i]

    return "_"


# Test
print(first_not_repeating_char("abacabad"))  # c
print(first_not_repeating_char("abacabaabacaba"))  # _
