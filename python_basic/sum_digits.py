#  Sum of digits
num = int(input("\nEnter a number to find sum of digits: "))
total = 0
temp = abs(num)
while temp:
    total += temp % 10
    temp //= 10
print(f"Sum of digits of {num} is {total}")