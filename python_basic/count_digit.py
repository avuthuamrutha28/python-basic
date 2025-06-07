# Count number of digits
num = int(input("Enter a number to count digits: "))
count = 0
temp = abs(num)
while temp:
    count += 1
    temp //= 10
print(f"Number of digits in {num} is {count}")