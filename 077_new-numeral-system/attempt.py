def new_numeral_system(number):
    result = []
    start_count = 65
    end_count = ord(number[0])

    while (start_count <= end_count):
        to_push = chr(start_count) + " + " + chr(end_count)
        result.append(to_push)
        start_count += 1
        end_count -= 1

    return result


# Test
print(new_numeral_system("G"))  # ["A + G", "B + F", "C + E", "D + D"]
