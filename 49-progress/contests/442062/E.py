'''
You are given an array consisting of all integers from [𝑙,𝑟]
 inclusive. For example, if 𝑙=2
 and 𝑟=5
, the array would be [2,3,4,5]
. What's the minimum number of elements you can delete to make the bitwise AND of the array non-zero?

A bitwise AND is a binary operation that takes two equal-length binary representations and performs the AND operation on each pair of the corresponding bits.

Input
The first line contains one integer 𝑡
 (1≤𝑡≤104
) — the number of test cases. Then 𝑡
 cases follow.

The first line of each test case contains two integers 𝑙
 and 𝑟
 (1≤𝑙≤𝑟≤2⋅105
) — the description of the array.

Output
For each test case, output a single integer — the answer to the problem.

Example
inputCopy
5
1 2
2 8
4 5
1 5
100000 200000
outputCopy
1
3
0
2
31072
Note
In the first test case, the array is [1,2]
. Currently, the bitwise AND is 0
, as 1 & 2=0
. However, after deleting 1
 (or 2
), the array becomes [2]
 (or [1]
), and the bitwise AND becomes 2
 (or 1
). This can be proven to be the optimal, so the answer is 1
.

In the second test case, the array is [2,3,4,5,6,7,8]
. Currently, the bitwise AND is 0
. However, after deleting 4
, 5
, and 8
, the array becomes [2,3,6,7]
, and the bitwise AND becomes 2
. This can be proven to be the optimal, so the answer is 3
. Note that there may be other ways to delete 3
 elements.


'''


def find_common_prefix(l, r):
    common_prefix = 0
    while l != r:
        l >>= 1
        r >>= 1
        common_prefix += 1
    return l << common_prefix

def count_trailing_zeros(n):
    count = 0
    while n & 1 == 0:
        n >>= 1
        count += 1
    return count

t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    common_prefix = find_common_prefix(l, r)
    if common_prefix > r:
        print(0)
    else:
        k = count_trailing_zeros(r - common_prefix)
        largest_number = common_prefix | (1 << k) - 1
        deleted_elements = r - largest_number + 1
        print(deleted_elements)