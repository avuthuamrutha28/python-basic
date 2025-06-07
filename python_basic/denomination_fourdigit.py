#  Denomination of four-digit number
num = int(input("\nEnter a 4-digit number to display denomination: "))
if 1000 <= num <= 9999:
    print(f"{num // 1000}*1000 = {(num // 1000) * 1000}")
    print(f"{(num % 1000) // 100}*100 = {((num % 1000) // 100) * 100}")
    print(f"{(num % 100) // 10}*10 = {((num % 100) // 10) * 10}")
    print(f"{num % 10}*1 = {(num % 10)}")
else:
    print("Not a 4-digit number")