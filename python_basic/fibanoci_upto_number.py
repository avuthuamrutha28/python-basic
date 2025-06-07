#  Fibonacci series up to 34
a, b = 0, 1
print("\nFibonacci series up to 34:")
while a <= 34:
    print(a, end=", ")
    a, b = b, a + b
print()