'''
Given an array of 𝑛
 positive integers 𝑎1,𝑎2,…,𝑎𝑛
 (1≤𝑎𝑖≤1000
). Find the maximum value of 𝑖+𝑗
 such that 𝑎𝑖
 and 𝑎𝑗
 are coprime,†
 or −1
 if no such 𝑖
, 𝑗
 exist.

For example consider the array [1,3,5,2,4,7,7]
. The maximum value of 𝑖+𝑗
 that can be obtained is 5+7
, since 𝑎5=4
 and 𝑎7=7
 are coprime.

†
 Two integers 𝑝
 and 𝑞
 are coprime if the only positive integer that is a divisor of both of them is 1
 (that is, their greatest common divisor is 1
).

Input
The input consists of multiple test cases. The first line contains an integer 𝑡
 (1≤𝑡≤10
) — the number of test cases. The description of the test cases follows.

The first line of each test case contains an integer 𝑛
 (2≤𝑛≤2⋅105
) — the length of the array.

The following line contains 𝑛
 space-separated positive integers 𝑎1
, 𝑎2
,..., 𝑎𝑛
 (1≤𝑎𝑖≤1000
) — the elements of the array.

It is guaranteed that the sum of 𝑛
 over all test cases does not exceed 2⋅105
.

Output
For each test case, output a single integer  — the maximum value of 𝑖+𝑗
 such that 𝑖
 and 𝑗
 satisfy the condition that 𝑎𝑖
 and 𝑎𝑗
 are coprime, or output −1
 in case no 𝑖
, 𝑗
 satisfy the condition.

Example
inputCopy
6
3
3 2 1
7
1 3 5 2 4 7 7
5
1 2 3 4 5
3
2 2 4
6
5 4 3 15 12 16
5
1 2 2 3 6
outputCopy
6
12
9
-1
10
7
Note
For the first test case, we can choose 𝑖=𝑗=3
, with sum of indices equal to 6
, since 1
 and 1
 are coprime.

For the second test case, we can choose 𝑖=7
 and 𝑗=5
, with sum of indices equal to 7+5=12
, since 7
 and 4
 are coprime.
'''

