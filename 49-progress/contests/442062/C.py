'''
You are given an array 𝑎
 of size 𝑛
.

You can perform the following operation on the array:

Choose two different integers 𝑖,𝑗
 (1≤𝑖<𝑗≤𝑛
), replace 𝑎𝑖
 with 𝑥
 and 𝑎𝑗
 with 𝑦
. In order not to break the array, 𝑎𝑖|𝑎𝑗=𝑥|𝑦
 must be held, where |
 denotes the bitwise OR operation. Notice that 𝑥
 and 𝑦
 are non-negative integers.
Please output the minimum sum of the array you can get after using the operation above any number of times.

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡
 (1≤𝑡≤1000)
. Description of the test cases follows.

The first line of each test case contains an integer 𝑛
 (2≤𝑛≤100)
 — the size of array 𝑎
.

The second line of each test case contains 𝑛
 integers 𝑎1,𝑎2,…,𝑎𝑛
 (0≤𝑎𝑖<230)
.

Output
For each test case, print one number in a line — the minimum possible sum of the array.

Example
inputCopy
4
3
1 3 2
5
1 2 4 8 16
2
6 6
3
3 5 6
outputCopy
3
31
6
7
Note
In the first example, you can perform the following operations to obtain the array [1,0,2]
:

1. choose 𝑖=1,𝑗=2
, change 𝑎1=1
 and 𝑎2=2
, it's valid since 1|3=1|2
. The array becomes [1,2,2]
.

2. choose 𝑖=2,𝑗=3
, change 𝑎2=0
 and 𝑎3=2
, it's valid since 2|2=0|2
. The array becomes [1,0,2]
.

We can prove that the minimum sum is 1+0+2=3
In the second example, We don't need any operations.


'''

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans |= a[i]
    print(ans)

