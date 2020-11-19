def internal_backups(last_backup_time, changes):
    result = []
    last_backup_times = {}

    for i in range(len(changes)):
        last_backup_times[changes[i][1]] = changes[i][0]

    keys = list(last_backup_times.keys())
    times = list(last_backup_times.values())
    for i in range(len(times)):
        if times[i] > last_backup_time:
            result.append(keys[i])

    return result


# Test
print(internal_backups(461620205, [
    [461620203, 1],
    [461620204, 2],
    [461620205, 6],
    [461620206, 5],
    [461620207, 3],
    [461620207, 5],
    [461620208, 1],
]))
