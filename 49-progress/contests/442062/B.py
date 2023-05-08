'''
You are given an integer 𝑛
. Check if 𝑛
 has an odd divisor, greater than one (does there exist such a number 𝑥
 (𝑥>1
) that 𝑛
 is divisible by 𝑥
 and 𝑥
 is odd).

For example, if 𝑛=6
, then there is 𝑥=3
. If 𝑛=4
, then such a number does not exist.

Input
The first line contains one integer 𝑡
 (1≤𝑡≤104
) — the number of test cases. Then 𝑡
 test cases follow.

Each test case contains one integer 𝑛
 (2≤𝑛≤1014
).

Please note, that the input for some test cases won't fit into 32
-bit integer type, so you should use at least 64
-bit integer type in your programming language.

Output
For each test case, output on a separate line:

"YES" if 𝑛
 has an odd divisor, greater than one;
"NO" otherwise.
You can output "YES" and "NO" in any case (for example, the strings yEs, yes, Yes and YES will be recognized as positive).

Example
inputCopy
6
2
3
4
5
998244353
1099511627776
outputCopy
NO
YES
NO
YES
YES
NO

'''

def isPowerOfTwo(n):
    return (n and (not(n & (n - 1))))

for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print('NO')
    elif isPowerOfTwo(n):
        print('NO')
    else:
        print('YES')

        