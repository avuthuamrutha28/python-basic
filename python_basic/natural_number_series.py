#  Natural number series and sum
num = int(input("\nEnter a number to print natural series and sum: "))
natural_sum = sum(range(1, num + 1))
print("Natural number series:", list(range(1, num + 1)))
print(f"Sum of series = {natural_sum}")
