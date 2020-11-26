def proper_noun_correction(inp):
    length = len(inp)
    return f"{inp[0].upper()}{inp[1:length].lower()}"


print(proper_noun_correction("pARis"))  # Paris
print(proper_noun_correction("John"))  # John
