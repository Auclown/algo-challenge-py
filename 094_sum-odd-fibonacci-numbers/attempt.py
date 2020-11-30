def sum_odd_fib(n):
    prev_n = 0
    curr_n = 1
    result = 0

    while (curr_n <= n):
        if curr_n % 2 != 0:
            result += curr_n

        curr_n += prev_n
        prev_n = curr_n - prev_n

    return result


# Test
print(sum_odd_fib(10))  # 10
print(sum_odd_fib(1000))  # 1785
print(sum_odd_fib(4000000))  # 4613732
