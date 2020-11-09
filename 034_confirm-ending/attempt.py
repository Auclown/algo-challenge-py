def confirm_ending(first_arg, target):
    cut_from = len(target) - 1

    return first_arg[cut_from:] == target


print(confirm_ending("Abstraction", "action"))  # True
print(confirm_ending("Open sesame", "pen"))  # False
