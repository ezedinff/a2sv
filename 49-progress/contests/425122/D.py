'''
D. New Sorting
time limit per test1 s.
memory limit per test256 MB
inputstandard input
outputstandard output
A student of 𝑧
-school found a kind of sorting called 𝑧
-sort. The array 𝑎
 with 𝑛
 elements are 𝑧
-sorted if two conditions hold:

𝑎𝑖≥𝑎𝑖−1
 for all even 𝑖
,
𝑎𝑖≤𝑎𝑖−1
 for all odd 𝑖>1
.
For example the arrays [1,2,1,2] and [1,1,1,1] are 𝑧
-sorted while the array [1,2,3,4] isn’t 𝑧
-sorted.

Can you make the array 𝑧
-sorted?

NB: the array is 1-indexed.

Input
The first line contains a single integer 𝑛
 (1≤𝑛≤1000
) — the number of elements in the array 𝑎
.

The second line contains 𝑛
 integers 𝑎𝑖
 (1≤𝑎𝑖≤109
) — the elements of the array 𝑎
.

Output
If it's possible to make the array 𝑎
 𝑧
-sorted print 𝑛
 space separated integers 𝑎𝑖
 — the elements after 𝑧
-sort. Otherwise print the only word "Impossible".

Examples
inputCopy
4
1 2 2 1
outputCopy
1 2 1 2
inputCopy
5
1 3 2 2 5
outputCopy
1 5 2 3 2

'''

def main():
    n = int(input().strip())
    a = list(map(int, input().split()))
    a.sort()
    ans = []
    for i in range(n//2):
        ans.append(a[i])
        ans.append(a[n-1-i])
    if n % 2 == 1:
        ans.append(a[n//2])
    print(' '.join(map(str, ans)))

    