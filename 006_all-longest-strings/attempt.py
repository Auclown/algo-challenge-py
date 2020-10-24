def all_longest_strings(input_array):
    longest_length = 0
    result = []
    for element in input_array:
        if (len(element) > longest_length):
            longest_length = len(element)

    for element in input_array:
        if (len(element) == longest_length):
            result.append(element)

    return result


# Test
print(all_longest_strings(["aba", "aa", "ad", "vcd", "aba"]))
# ["aba", "vcd", "aba"]
print(all_longest_strings(["abada", "aa", "ad", "vcd", "abada"]))
# ['abada','abada']
print(all_longest_strings(["abadadada", "aa", "ad", "vcd", "abada"]))
# ['abadadada']
print(all_longest_strings(["a", "aa", "ad", "v", "b"]))
# ['aa','ad']
