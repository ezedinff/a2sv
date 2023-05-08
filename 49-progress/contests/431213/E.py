'''
You are given an array 𝑎1,𝑎2,…,𝑎𝑛
 consisting of integers from 0
 to 9
. A subarray 𝑎𝑙,𝑎𝑙+1,𝑎𝑙+2,…,𝑎𝑟−1,𝑎𝑟
 is good if the sum of elements of this subarray is equal to the length of this subarray (∑𝑖=𝑙𝑟𝑎𝑖=𝑟−𝑙+1
).

For example, if 𝑎=[1,2,0]
, then there are 3
 good subarrays: 𝑎1…1=[1],𝑎2…3=[2,0]
 and 𝑎1…3=[1,2,0]
.

Calculate the number of good subarrays of the array 𝑎
.

Input
The first line contains one integer 𝑡
 (1≤𝑡≤1000
) — the number of test cases.

The first line of each test case contains one integer 𝑛
 (1≤𝑛≤105
) — the length of the array 𝑎
.

The second line of each test case contains a string consisting of 𝑛
 decimal digits, where the 𝑖
-th digit is equal to the value of 𝑎𝑖
.

It is guaranteed that the sum of 𝑛
 over all test cases does not exceed 105
.

Output
For each test case print one integer — the number of good subarrays of the array 𝑎
.

Example
inputCopy
3
3
120
5
11011
6
600005
outputCopy
3
6
1
Note
The first test case is considered in the statement.

In the second test case, there are 6
 good subarrays: 𝑎1…1
, 𝑎2…2
, 𝑎1…2
, 𝑎4…4
, 𝑎5…5
 and 𝑎4…5
.

In the third test case there is only one good subarray: 𝑎2…6.
'''

from collections import defaultdict

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        n = int(input())
        a = list(map(int,list(input())))
        for i in range(n):
            a[i] -= 1
        for i in range(1, n):
            a[i] += a[i - 1]
        d = defaultdict(int)
        d[0] = 1
        ans = 0
        for i in a:
            if i in d:
                ans += d[i]
                d[i] += 1
            else:
                d[i] += 1
        print(ans)

'''
The problem asks us to find the number of good subarrays in an array.
A subarray 𝑎𝑙,𝑎𝑙+1,𝑎𝑙+2,…,𝑎𝑟−1,𝑎𝑟
is good if the sum of its elements is equal to its length, i.e., ∑𝑖=𝑙𝑟𝑎𝑖=𝑟−𝑙+1.

For example, [1,2,0] has 3 good subarrays: [1], [2,0], and [1,2,0].

The solution to this problem uses a defaultdict to store the frequency
of the sum of subarrays seen so far. We first subtract 1 from each element of
the array, so that the sum of a subarray of length k is k - sum of elements.
Then, we calculate the prefix sum of the modified array, i.e., the sum of elements
from the beginning of the array up to each index i. Let the prefix sum at index i be x.
If there exists an index j<i such that the prefix sum at index j is x, then the sum of elements
from j+1 to i is equal to the length of the subarray, and hence it is a good subarray.
We keep a count of the number of such subarrays seen so far and add it to the answer
for the current array.

Here is the step-by-step explanation of the solution:

Read the number of test cases.
For each test case:
a. Read the length of the array and the array itself.
b. Subtract 1 from each element of the array.
c. Calculate the prefix sum of the modified array.
d. Initialize a defaultdict to store the frequency of the prefix sums seen so far. Set the frequency of 0 to 1, as the sum of the empty subarray is 0.
e. Initialize the answer to 0.
f. Loop through the prefix sums and update the frequency in the defaultdict.
If a prefix sum has been seen before, the sum of all subarrays ending at the current index and having a length equal to the difference between the current index and the index of the previous occurrence of the prefix sum is a good subarray. Add the frequency of the prefix sum to the answer.
g. Print the answer.
Overall, the time complexity of this solution is O(n), where n is the length of the array.

'''