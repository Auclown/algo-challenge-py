def incorrect_password_attempt(passcode, attempts):
    for i in range(len(attempts)):
        if (i < 10 and attempts[i] == passcode):
            return True
        else:
            return False


# Test
print(incorrect_password_attempt("1111", ["1111", "4444",
                                          "9999", "3333",
                                          "8888", "2222",
                                          "7777", "0000",
                                          "6666", "7285",
                                          "5555", "1111"]))
# True
