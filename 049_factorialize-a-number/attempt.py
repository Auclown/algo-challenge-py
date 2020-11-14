def fact_a_number(n):
    if n < 1:
        return 1

    return n * fact_a_number(n - 1)


# Test
print(fact_a_number(5))  # 120
print(fact_a_number(10))  # 3628800
