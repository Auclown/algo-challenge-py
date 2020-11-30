def unique_digit_products(a):
    products = []

    for i in range(len(a)):
        _product = product(a[i])

        if (not _product in products):
            products.append(_product)

    return len(products)


def product(n):
    result = 1
    digits = list(str(n))

    for digit in digits:
        result *= int(digit)

    return result


print(unique_digit_products([2, 8, 121, 42, 222, 23]))  # 3
