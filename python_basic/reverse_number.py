#  Reverse of the number
num = int(input("\nEnter a number to reverse: "))
reverse = 0
temp = abs(num)
while temp:
    reverse = reverse * 10 + temp % 10
    temp //= 10
print(f"Reverse of {num} is {reverse if num >= 0 else -reverse}")