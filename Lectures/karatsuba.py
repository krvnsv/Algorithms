def karatsuba(num1, num2):
    if num1 < 10 or num2 < 10:
        return num1 * num2

    n = max(len(str(num1)), len(str(num2)))

    m = n // 2

    divisor = 10 ** m

    high1 = num1 // divisor  # a - high part of num1
    low1 = num1 % divisor    # b - low part of num1
    high2 = num2 // divisor  # c - high part of num2
    low2 = num2 % divisor    # d - low part of num2

    z0 = karatsuba(low1, low2)                  # bd - product of low parts
    z1 = karatsuba(low1 + high1, low2 + high2)  # pq - (a+b)*(c+d)
    z2 = karatsuba(high1, high2)                # ac - product of high parts

    # Final formula: ac * 10^(2m) + adbc * 10^m + bd
    return (z2 * 10 ** (2 * m)) + ((z1 - z2 - z0) * 10 ** m) + z0  # (ac * 10^(2m)) + (adbc * 10^m) + bd

print(karatsuba(100, 111))  # 11100
print(karatsuba(12345, 6789))  # 83797005