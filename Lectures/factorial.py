# 3! -> 1 * 2 * 3

def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
for i in range(10):
    print(factorial(i))