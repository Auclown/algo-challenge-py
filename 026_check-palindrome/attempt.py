def check_palindrome(inp_str):
    inp_str = inp_str.lower()
    rvsd_str = inp_str[::-1]

    return inp_str == rvsd_str


# Test
print(check_palindrome("aabaa"))  # True
print(check_palindrome("abac"))  # False
print(check_palindrome("a"))  # True
