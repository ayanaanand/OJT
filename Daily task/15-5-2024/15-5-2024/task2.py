def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

# Example: Generate Fibonacci series up to the 10th number
fib_series_10 = fibonacci(10)
print(fib_series_10)