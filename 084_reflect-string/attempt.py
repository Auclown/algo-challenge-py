def reflect_string(inp_string):
    result = ""
    reflections = {
        "a": "z", "b": "y", "c": "x", "d": "w", "e": "v", "f": "u", "g": "t",
        "h": "s", "i": "r", "j": "q", "k": "p", "l": "o", "m": "n", "n": "m",
        "o": "l", "p": "k", "q": "j", "r": "i", "s": "h", "t": "g", "u": "f",
        "v": "e", "w": "d", "x": "c", "y": "b", "z": "a",
    }

    for i in range(len(inp_string)):
        result += reflections[inp_string[i]]

    return result


# Test
print(reflect_string("name"))  # mznv
