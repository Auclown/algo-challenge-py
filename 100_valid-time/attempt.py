def valid_time(time):
    hours = int(time.split(":")[0])
    minutes = int(time.split(":")[1])

    if minutes > 60 or hours > 24:
        return False

    return True


print(valid_time("13:58"))  # True
print(valid_time("25:51"))  # False
print(valid_time("02:76"))  # False
