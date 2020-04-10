# Fibonacci numbers

# Returns fibonacci sequence with a length of n
def fibonacci(n):
    fib = [0, 1]
    for i in range(0,n):
        suma = fib[i] + fib[i+1]
        fib.append(suma)
    return fib

# Returns n-th fibonacci number
def fibonacci_last(n):
    fib = [0, 1]
    for i in range(2, n):
        fib_i = fib[i-2] + fib[i-1]
        fib.append(fib_i)
    return fib[n]

print(fibonacci(4))
