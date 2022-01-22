# a binary tree is a data structure that characterized by the following properties:
# it can be an empty tree where the root is null
# it can consist of a root node that contains a value and two subtrees, left subtree and right subtree

# Given an integer, determine the number of valid binary search trees that can be created by nodes numbered 1 to n.

# function description:
# complete the function numBSTs that has the following parameters:
# numBSTs has the following parameters:
# int nodeValues[n]: an array of integers representing the values of the nodes
# returns:
# int[n]: an array of integers represent the number of different binary search trees that can be created for each test case.
# since the number may be very large, return the number modulo 1000000007

# constraints:
# 1 <= n <= 1000
# 1 <= nodeValues[i] <= 1000

# test cases
# nodeValues = [5, 1, 2, 3, 4, 100]
# output = [1, 2, 5, 14, 25666077]

def numBSTs(nodeValues):
    # Write your code here
    # This is a "method-only" submission.
    # You only need to complete this method.
    mod = 1000000007
    n = len(nodeValues)
    dp = [[0] * n for i in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n - 1):
        for j in range(i + 1, n):
            for k in range(i, j):
                dp[i][j] += dp[i][k] * dp[k + 1][j]
    return [dp[0][n - 1] % mod for i in range(n)]

print(numBSTs([5, 1, 2, 3, 4, 100]))