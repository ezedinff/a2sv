'''
E. No Zero
time limit per test1 s.
memory limit per test256 MB
inputstandard input
outputstandard output
You are given an array of 𝑛
 integers 𝑎1,𝑎2,…,𝑎𝑛
.

You have to create an array of 𝑛
 integers 𝑏1,𝑏2,…,𝑏𝑛
 such that:

The array 𝑏
 is a rearrangement of the array 𝑎
, that is, it contains the same values and each value appears the same number of times in the two arrays. In other words, the multisets {𝑎1,𝑎2,…,𝑎𝑛}
 and {𝑏1,𝑏2,…,𝑏𝑛}
 are equal.
For example, if 𝑎=[1,−1,0,1]
, then 𝑏=[−1,1,1,0]
 and 𝑏=[0,1,−1,1]
 are rearrangements of 𝑎
, but 𝑏=[1,−1,−1,0]
 and 𝑏=[1,0,2,−3]
 are not rearrangements of 𝑎
.

For all 𝑘=1,2,…,𝑛
 the sum of the first 𝑘
 elements of 𝑏
 is nonzero. Formally, for all 𝑘=1,2,…,𝑛
, it must hold
𝑏1+𝑏2+⋯+𝑏𝑘≠0.
If an array 𝑏1,𝑏2,…,𝑏𝑛
 with the required properties does not exist, you have to print NO.

Input
Each test contains multiple test cases. The first line contains an integer 𝑡
 (1≤𝑡≤1000
) — the number of test cases. The description of the test cases follows.

The first line of each testcase contains one integer 𝑛
 (1≤𝑛≤50
)  — the length of the array 𝑎
.

The second line of each testcase contains 𝑛
 integers 𝑎1,𝑎2,…,𝑎𝑛
 (−50≤𝑎𝑖≤50
)  — the elements of 𝑎
.

Output
For each testcase, if there is not an array 𝑏1,𝑏2,…,𝑏𝑛
 with the required properties, print a single line with the word NO.

Otherwise print a line with the word YES, followed by a line with the 𝑛
 integers 𝑏1,𝑏2,…,𝑏𝑛
.

If there is more than one array 𝑏1,𝑏2,…,𝑏𝑛
 satisfying the required properties, you can print any of them.

Example
inputCopy
4
4
1 -2 3 -4
3
0 0 0
5
1 -1 1 -1 1
6
40 -31 -9 0 13 -40
outputCopy
YES
1 -2 3 -4
NO
YES
1 1 -1 1 -1
YES
-40 13 40 0 -9 -31
Note
Explanation of the first testcase: An array with the desired properties is 𝑏=[1,−2,3,−4]
. For this array, it holds:

The first element of 𝑏
 is 1
.
The sum of the first two elements of 𝑏
 is −1
.
The sum of the first three elements of 𝑏
 is 2
.
The sum of the first four elements of 𝑏
 is −2
.
Explanation of the second testcase: Since all values in 𝑎
 are 0
, any rearrangement 𝑏
 of 𝑎
 will have all elements equal to 0
 and therefore it clearly cannot satisfy the second property described in the statement (for example because 𝑏1=0
). Hence in this case the answer is NO.

Explanation of the third testcase: An array with the desired properties is 𝑏=[1,1,−1,1,−1]
. For this array, it holds:

The first element of 𝑏
 is 1
.
The sum of the first two elements of 𝑏
 is 2
.
The sum of the first three elements of 𝑏
 is 1
.
The sum of the first four elements of 𝑏
 is 2
.
The sum of the first five elements of 𝑏
 is 1
.
Explanation of the fourth testcase: An array with the desired properties is 𝑏=[−40,13,40,0,−9,−31]
. For this array, it holds:

The first element of 𝑏
 is −40
.
The sum of the first two elements of 𝑏
 is −27
.
The sum of the first three elements of 𝑏
 is 13
.
The sum of the first four elements of 𝑏
 is 13
.
The sum of the first five elements of 𝑏
 is 4
.
The sum of the first six elements of 𝑏
 is −27
.

'''
import unittest

def solve(a, n):
    if sum(a) == 0:
        return 'NO'
    return 'YES'
    if sum(a) > 0:
        a.sort(reverse=True)
    else:
        a.sort()
    print(*a)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(a, n))

class Test(unittest.TestCase):
    def test(self):
        assert solve([1, -2, 3, -4], 4) == 'YES'
        assert solve([0, 0, 0], 3) == 'NO'

if __name__ == '__main__':
    unittest.main()