def common_character_count(s1, s2):
    chars = {}
    count = 0

    for i in range(len(s1)):
        if (not s1[i] in chars):
            chars[s1[i]] = 1
        else:
            chars[s1[i]] += 1

    for j in range(len(s2)):
        if (not s2[j] in chars):
            chars[s2[j]] = 1
        else:
            chars[s2[j]] += 1

    # print(chars)
    for _, value in chars.items():
        if value > 1:
            count += 1

    return count


# Test
print(common_character_count("aabcc", "adcaa"))  # 3
