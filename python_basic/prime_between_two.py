#  Prime numbers between two numbers
start = int(input("\nEnter the start number: "))
end = int(input("Enter the end number: "))
print(f"Prime numbers between {start} and {end}:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
print()