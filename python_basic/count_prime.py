#  Count of prime digits
num = input("\nEnter a number to count prime digits: ")
prime_digits = {'2', '3', '5', '7'}
count = sum(1 for digit in num if digit in prime_digits)
print(f"Count of prime digits in {num} is {count}")
