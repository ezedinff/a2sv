'''
Yared gave you an array 𝑎
 that contains 𝑛
 positive integers (≥0
) and he told you, in one move, you can select two different indices 𝑖
 and 𝑗
 (𝑖≠𝑗
) such that the absolute difference between the corresponding elements 𝑎𝑖
 and 𝑎𝑗
 is less than or equal to one (|𝑎𝑖−𝑎𝑗|≤1
) and remove the smaller of these two elements. If two elements are equal, you can remove either one of them but not both.

Your goal is to determine whether it is possible to obtain an array with only one element by performing multiple moves (possibly zero).

Input
The first line of the input contains one integer 𝑡
 (1≤𝑡≤1000
) — the number of test cases. Then 𝑡
 test cases follow.

The first line of the test case contains one integer 𝑛
 (1≤𝑛≤50
) — the length of 𝑎
. The second line of the test case contains 𝑛
 integers 𝑎1,𝑎2,…,𝑎𝑛
 (1≤𝑎𝑖≤100
), where 𝑎𝑖
 is the 𝑖
-th element of 𝑎
.

Output
For each test case, print "YES" if it is possible to obtain an array of one element,
or "NO" otherwise.
'''

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    stack = []
    for x in a:
        while stack and x - stack[-1] <= 1:
            stack.pop()
        stack.append(x)
    print('YES' if len(stack) == 1 else 'NO')


# improved solution
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1, n):
        if a[i] - a[i - 1] > 1:
            print('NO')
            break
    else:
        print('YES')