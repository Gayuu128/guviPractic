from functools import reduce

n = int(input("Enter a number : "))

# Lambda function to generate Fibonacci series
fibonacci = lambda n: reduce(
    lambda seq, _: seq + [seq[-1] + seq[-2]],
    range(n - 2),
    [0, 1]
) if n > 1 else [0]

print("Fibonacci series:", fibonacci(n))
