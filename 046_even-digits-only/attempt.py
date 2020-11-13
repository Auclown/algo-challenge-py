def even_digits_only(n):
    s = str(n)

    for i in range(len(s)):
        if (int(s[i]) % 2 != 0):
            return False

    return True


# Test
print(even_digits_only(248622))  # True
print(even_digits_only(642386))  # False
