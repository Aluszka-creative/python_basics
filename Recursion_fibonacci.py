# Fibonacci numbers made with recursion

def fibonacci(n):
    if n == 0:
        return  0
    elif n == 1:
        return 1
    elif n >= 2:
        fibonacci_number = fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci_number


for n in range(0, 9):
    print(fibonacci(n))