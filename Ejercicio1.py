def factorial (n):
    if n < 0:
        return "El factoria del números negativos no está definido"
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(-2))
print(factorial(0))
print(factorial(4))
