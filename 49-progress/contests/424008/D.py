'''
D. Triangle
time limit per test1.0 s
memory limit per test256 MB
inputstandard input
outputstandard output
Mahmoud has 𝑛
 line segments, the 𝑖
-th of them has length 𝑎𝑖
. Ehab challenged him to use exactly 3
 line segments to form a non-degenerate triangle. Mahmoud doesn't accept challenges unless he is sure he can win, so he asked you to tell him if he should accept the challenge.
  Given the lengths of the line segments, check if he can choose exactly 3
 of them to form a non-degenerate triangle.

Mahmoud should use exactly 3
 line segments, he can't concatenate two line segments or change any length. A non-degenerate triangle is a triangle with positive area.

Input
The first line contains single integer 𝑛
 (3≤𝑛≤105
) — the number of line segments Mahmoud has.

The second line contains 𝑛
 integers 𝑎1,𝑎2,…,𝑎𝑛
 (1≤𝑎𝑖≤109
) — the lengths of line segments Mahmoud has.

Output
In the only line print "YES" if he can choose exactly three line segments and form a non-degenerate triangle with them, and "NO" otherwise.

Examples
inputCopy
5
1 5 3 2 4
outputCopy
YES
inputCopy
3
4 1 2
outputCopy
NO

'''

from typing import List

def get_inputs() -> List[int]:
    n = int(input())
    a = list(map(int, input().split()))
    return [n, a]

def canFormTriangle(a: List[int]) -> bool:
    a.sort()
    for i in range(len(a) - 2):
        if a[i] + a[i + 1] > a[i + 2]:
            return True
    return False
# explanation:
# if the sum of the smallest two elements is greater than the largest element, then we can form a triangle

# why till i + 2?
# because we need to check if the sum of the smallest two elements is greater than the largest element

def main():
    n, a = get_inputs()
    print('YES' if canFormTriangle(a) else 'NO')

# why sort the array?
# because if we sort the array,
# we can check if the sum of the smallest two elements is greater than the largest element

if __name__ == '__main__':
    main()