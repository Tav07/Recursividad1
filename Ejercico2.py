def fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        return "Solo se aceptan números positivos"
    return (n-1) + (n-2)

print(fibonacci(4))