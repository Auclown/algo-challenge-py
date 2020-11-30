def square_digits_sequence(a0):
    seq = [a0]
    while seq[-1] not in seq[:-1]:
        seq.append(sum(int(i)**2 for i in str(seq[-1])))

    return len(seq)


# Test
print(square_digits_sequence(16))  # 9
print(square_digits_sequence(103)) # 4