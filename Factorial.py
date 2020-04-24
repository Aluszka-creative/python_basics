# Factorial

def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        factorial_number = 1
        for i in range(2, n+1):
            factorial_number *= i

        return factorial_number
