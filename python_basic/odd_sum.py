# 8. Odd number series and sum
n = int(input("\nEnter a number to display odd series and its sum: "))
odd_series = list(range(1, n + 1, 2))
print("Odd number series:", odd_series)
print(f"Sum of odd series = {sum(odd_series)}")
