def add_border(picture):
    result = []
    length = len(picture[0])
    border = ""

    for _ in range(length + 2):
        border += "*"

    for i in range(len(picture)):
        new_pic = "*" + picture[i]
        new_pic = new_pic + "*"
        result.append(new_pic)

    result.insert(0, border)
    result.append(border)

    return result


# Test
print(add_border(["abc",
                  "ded"]))
