def sort_by_length(strings):
    return sorted(strings, key=len)


# Test
print(sort_by_length(["abc", "", "aaa", "a", "zz"]))
# ["", "a", "zz", "abc", "aaa"]
