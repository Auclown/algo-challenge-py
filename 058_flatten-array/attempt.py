def flatten_array(inp_array):
    if (len(inp_array) == 0):
        return inp_array

    if isinstance(inp_array[0], list):
        return flatten_array(inp_array[0]) + flatten_array(inp_array[1:])

    return inp_array[:1] + flatten_array(inp_array[1:])


# Test
print(flatten_array([[["a"]], [["b"]]]))  # [a, b]
print(flatten_array([1, [2], [3, [[4]]]]))  # [1, 2, 3, 4]
