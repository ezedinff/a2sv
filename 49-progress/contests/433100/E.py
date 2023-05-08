'''
Jon fought bravely to rescue the wildlings who were attacked by the white-walkers at Hardhome. On his arrival, Sam tells him that he wants to go to Oldtown to train at the Citadel to become a maester, so he can return and take the deceased Aemon's place as maester of Castle Black. Jon agrees to Sam's proposal and Sam sets off his journey to the Citadel. However becoming a trainee at the Citadel is not a cakewalk and hence the maesters at the Citadel gave Sam a problem to test his eligibility.

Initially Sam has a list with a single element n. Then he has to perform certain operations on this list. In each operation Sam must remove any element x, such that x > 1, from the list and insert at the same position , ,  sequentially. He must continue with these operations until all the elements in the list are either 0 or 1.

Now the masters want the total number of 1s in the range l to r (1-indexed). Sam wants to become a maester but unfortunately he cannot solve this problem. Can you help Sam to pass the eligibility test?

input
The first line contains three integers n, l, r (0 ≤ n < 250, 0 ≤ r - l ≤ 105, r ≥ 1, l ≥ 1) – initial element and the range l to r.

It is guaranteed that r is not greater than the length of the final list.

Output
Output the total number of 1s in the range l to r in the final sequence.

input
7 2 5
output
4
input
10 3 10
output
5

Note
Consider first example:

[7]→[3,1,3]→[1,1,1,1,3]→[1,1,1,1,1,1,1]→[1,1,1,1,1,1,1]
Elements on positions from 2
-nd to 5
-th in list is [1,1,1,1]
. The number of ones is 4
.

For the second example:

[10]→[1,0,1,1,1,0,1,0,1,0,1,1,1,0,1]
Elements on positions from 3
-rd to 10
-th in list is [1,1,1,0,1,0,1,0]
. The number of ones is 5
.
'''

def main():
    # get input values and store them in variables
    n, left, right = map(int, input().strip().split())

    # calculate the total number of nodes in the tree
    num_nodes, total = n, 0
    while num_nodes > 0:
        total = total*2 + 1
        num_nodes //= 2
    
    # recursive function to find the number of nodes in a given range
    def range_finder(left, right, node_num, left_num, right_num):
        # if the range is outside of the current node or the node is empty, return 0
        if right_num < left or right < left_num or node_num == 0:
            return 0
        # if the node is a leaf, return 1
        if node_num == 1:
            return 1
        # otherwise, split the node into its two children and recursively search them
        mid_num = (left_num + right_num) // 2
        return range_finder(left, right, node_num//2, left_num, mid_num-1) + range_finder(left, right, node_num%2, mid_num, mid_num) + range_finder(left, right, node_num//2, mid_num+1, right_num)
    
    # call the range_finder function and print the result
    print(range_finder(left, right, n, 1, total))


def main():
    n, left, right = map(int, input().strip().split())
    num_nodes, total = n, 0
    while num_nodes > 0:
        total = total*2 + 1
        num_nodes //= 2
    def range_finder(left, right, node_num, left_num, right_num):
        if right_num < left or right < left_num or node_num == 0:
            return 0
        if node_num == 1:
            return 1
        mid_num = (left_num + right_num) // 2
        l = range_finder(left, right, node_num//2, left_num, mid_num-1)
        m = range_finder(left, right, node_num%2, mid_num, mid_num)
        r = range_finder(left, right, node_num//2, mid_num+1, right_num)
        return l + m + r
    
    print(range_finder(left, right, n, 1, total))