# a binary tree is a data structure that characterized by the following properties:
# it can be an empty tree where the root is null
# it can consist of a root node that contains a value and two subtrees, left subtree and right subtree

# Given an integer, determine the number of valid BSTs that can be created by nodes numbered from 1 to that integer. please see the samples below for diagrams based on 1, 2 or 3 nodes.
# for example:
# nodeValues = [5, 1, 2, 3, 4, 100]
# where the first number is the size of the BST
# the number of valid BSTs is: [1, 2, 5, 14, 25666077]

# If there are n nodes then the number of possible binary trees is (1/n+1)*(2n^Cn)

def numBST(n):
    # DP to store the number of unique
    # BST with key i 
    dp = [0] * (n + 1) 
    m = 1000000007
    # Base case 
    dp[0], dp[1] = 1, 1
  
    # fill the dp table in top-down 
    # approach. 
    for i in range(2, n + 1): 
        for j in range(1, i + 1): 
  
            # n-i in right * i-1 in left 
            dp[i] = dp[i] + (dp[i - j] *
                             dp[j - 1]) 
  
    return dp[n] % m

def numBSTs(nodeValues):
    nodes = nodeValues[1:]
    return [numBST(n) for n in nodes]

print(numBSTs([5, 1, 2, 3, 4, 100]))