#  Factorial using while loop
num = int(input("\nEnter a number to find factorial using while loop: "))
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1
print(f"Factorial of {num} is {factorial}")