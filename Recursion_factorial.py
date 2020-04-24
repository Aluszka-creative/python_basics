# Factorial made with recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n >= 2:
        result = n * factorial(n - 1)
    return  result

for n in range(0, 5):
    print(factorial(n))