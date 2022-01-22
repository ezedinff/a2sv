# closestNumbers.py
# given an array of distinct integers, determine the minimum absolute difference between any two of them. print all elements pairs with the minimum difference in ascending order.
# Example:
# numbers = [6, 2, 4, 10]
# prints:
# 2 4
# 4 6
def closestNumbers(numbers):
    numbers.sort()
    min_diff = float('inf')
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff == min_diff:
            print(numbers[i], numbers[i + 1])

closestNumbers([6, 2, 4, 10])
