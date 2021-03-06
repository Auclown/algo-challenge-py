def stolen_lunch(note):
    result = ""
    code_dict = {
        "a": "0", "b": "1", "c": "2", "d": "3", "e": "4",
        "f": "5", "g": "6", "h": "7", "i": "8", "j": "9",
        "0": "a", "1": "b", "2": "c", "3": "d", "4": "e",
        "5": "f", "6": "g", "7": "h", "8": "i", "9": "j",
    }

    chars = list(note)

    for i in range(len(chars)):
        to_add = code_dict[chars[i]] if chars[i] in code_dict else chars[i]
        result += to_add

    return result


# Test
print(stolen_lunch("you'll n4v4r 6u4ss 8t: cdja"))
# you'll never guess it: 2390
