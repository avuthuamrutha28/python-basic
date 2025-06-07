#  Armstrong number check
num = int(input("\nEnter a number to check if it's Armstrong: "))
num_str = str(num)
n = len(num_str)
armstrong_sum = sum(int(digit) ** n for digit in num_str)
print("Armstrong number" if armstrong_sum == num else "Not an Armstrong number")