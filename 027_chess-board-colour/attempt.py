def chess_board_colour(cell_one, cell_two):
    cell_one_colour = ""
    cell_two_colour = ""

    char_group_one = ["a", "c", "e", "g"]
    char_group_two = ["b", "d", "f", "h"]

    one_char = cell_one[0].lower()
    one_numb = cell_one[1]
    two_char = cell_two[0].lower()
    two_numb = cell_two[1]

    if one_char in char_group_one:
        if int(one_numb) % 2 == 0:
            cell_one_colour = "black"
        else:
            cell_one_colour = "white"

    if one_char in char_group_two:
        if int(one_numb) % 2 == 0:
            cell_one_colour = "white"
        else:
            cell_one_colour = "black"

    if two_char in char_group_one:
        if int(two_numb) % 2 == 0:
            cell_two_colour = "black"
        else:
            cell_two_colour = "white"

    if two_char in char_group_two:
        if int(two_numb) % 2 == 0:
            cell_two_colour = "white"
        else:
            cell_two_colour = "black"

    return cell_one_colour == cell_two_colour


# Test
print(chess_board_colour("A1", "C3"))  # True
print(chess_board_colour("A1", "H3"))  # False
