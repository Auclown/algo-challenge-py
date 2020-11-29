def sum_all_primes(n):
    result = 0
    for i in range(1, n):
        if is_prime(i):
            result += i

    return result


def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# Test
print(sum_all_primes(10))  # 17
