#  Sum of even and odd numbers up to the given number
num = int(input("\nEnter a number to calculate even and odd sums: "))
even_sum = sum(i for i in range(0, num + 1, 2))
odd_sum = sum(i for i in range(1, num + 1, 2))
print(f"Sum of even numbers = {even_sum}")
print(f"Sum of odd numbers = {odd_sum}")