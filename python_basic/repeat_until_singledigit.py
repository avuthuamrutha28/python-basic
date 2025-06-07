#  Repeated sum to single digit
num = int(input("\nEnter a number to find repeated sum to single digit: "))
while num >= 10:
    num = sum(int(digit) for digit in str(num))
print(f"Single digit sum is {num}")
