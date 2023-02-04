'''
B. Maximum Sum
time limit per test1.0 s
memory limit per test256 MB
inputstandard input
outputstandard output
Once Bob got to a sale of old TV sets. There were 𝑛
 TV sets at that sale. TV set with index 𝑖
 costs 𝑎𝑖
 bellars. Some TV sets have a negative price — their owners are ready to pay Bob if he buys their useless apparatus. Bob can «buy» any TV sets he wants. Though he's very strong, Bob can carry at most 𝑚
 TV sets, and he has no desire to go to the sale for the second time. Please, help Bob find out the maximum sum of money that he can earn.

Input
The first line contains two space-separated integers 𝑛
 and 𝑚
 (1≤𝑚≤𝑛≤100
) — amount of TV sets at the sale, and amount of TV sets that Bob can carry. The following line contains 𝑛
 space-separated integers 𝑎𝑖
 (−1000≤𝑎𝑖≤1000
) — prices of the TV sets.

Output
Output the only number — the maximum sum of money that Bob can earn, given that he can carry at most 𝑚
 TV sets.

Examples
inputCopy
5 3
-6 0 35 -2 4
outputCopy
8
inputCopy
4 2
7 0 0 -7
outputCopy
7
'''

def solve(n, m, a):
    a.sort()
    ans = 0
    for i in range(m):
        if a[i] < 0:
            ans += a[i]
    return -ans

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, m, a))