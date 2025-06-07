#  Increment each digit of a 5-digit number by 1
num = input("\nEnter a 5-digit number to increment each digit by 1: ")
if len(num) == 5 and num.isdigit():
    incremented = ''.join(str((int(digit) + 1) % 10) for digit in num)
    print(f"Incremented number: {incremented}")
else:
    print("Invalid input. Please enter a 5-digit number.")
