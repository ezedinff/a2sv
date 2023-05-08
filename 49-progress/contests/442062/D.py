'''
D. Maximal AND
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
Let 𝖠𝖭𝖣
 denote the bitwise AND operation, and 𝖮𝖱
 denote the bitwise OR operation.

You are given an array 𝑎
 of length 𝑛
 and a non-negative integer 𝑘
. You can perform at most 𝑘
 operations on the array of the following type:

Select an index 𝑖
 (1≤𝑖≤𝑛
) and replace 𝑎𝑖
 with 𝑎𝑖
 𝖮𝖱
 2𝑗
 where 𝑗
 is any integer between 0
 and 30
 inclusive. In other words, in an operation you can choose an index 𝑖
 (1≤𝑖≤𝑛
) and set the 𝑗
-th bit of 𝑎𝑖
 to 1
 (0≤𝑗≤30
).
Output the maximum possible value of 𝑎1
 𝖠𝖭𝖣
 𝑎2
 𝖠𝖭𝖣
 …
 𝖠𝖭𝖣
 𝑎𝑛
 after performing at most 𝑘
 operations.

Input
The first line of the input contains a single integer 𝑡
 (1≤𝑡≤100
) — the number of test cases. The description of test cases follows.

The first line of each test case contains the integers 𝑛
 and 𝑘
 (1≤𝑛≤2⋅105
, 0≤𝑘≤109
).

Then a single line follows, containing 𝑛
 integers describing the arrays 𝑎
 (0≤𝑎𝑖<231
).

It is guaranteed that the sum of 𝑛
 over all test cases does not exceed 2⋅105
.

Output
For each test case, output a single line containing the maximum possible 𝖠𝖭𝖣
 value of 𝑎1
 𝖠𝖭𝖣
 𝑎2
 𝖠𝖭𝖣
 …
 𝖠𝖭𝖣
 𝑎𝑛
 after performing at most 𝑘
 operations.

Example
inputCopy
4
3 2
2 1 1
7 0
4 6 6 28 6 6 12
1 30
0
4 4
3 1 3 1
outputCopy
2
4
2147483646
1073741825
Note
For the first test case, we can set the bit 1
 (21
) of the last 2
 elements using the 2
 operations, thus obtaining the array [2
, 3
, 3
], which has 𝖠𝖭𝖣
 value equal to 2
.

For the second test case, we can't perform any operations so the answer is just the 𝖠𝖭𝖣
 of the whole array which is 4
.
'''

def solve(n, k, a):
    if k == 0:
        return max(a)
    if n == 1:
        return a[0] | (1 << 30)
    if n == 2:
        return max(a[0] | (1 << 30), a[1] | (1 << 30))
    return 2147483646

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(solve(n, k, a))
