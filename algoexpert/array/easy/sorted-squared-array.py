# Sorted Squared Array
# https://www.algoexpert.io/questions/Sorted%20Squared%20Array
# Write a function that takes in a non-empty array of integers that are sorted in
# ascending order and returns a new array of the same length with the squares of
# the original integers also sorted in ascending order.
# Sample Input
# array = [1, 2, 3, 5, 6, 8, 9]
# Sample Output
# [1, 4, 9, 25, 36, 64, 81]


def sortedSquaredArray(array):
    ans = []
    for num in array:
        ans.append(num * num)
    return ans

if __name__ == '__main__':
    print(sortedSquaredArray([1, 2, 3, 5, 6, 8, 9]))