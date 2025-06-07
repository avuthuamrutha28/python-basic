#  Prime number check
num = int(input("\nEnter a number to check if it's prime: "))
if num < 2:
    print("Not a prime number")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")