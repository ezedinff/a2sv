# https://codeforces.com/problemset/problem/977/C

from collections import Counter

def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(solve(n, k, nums))

def solve(n, k, nums):
    nums.sort()
    if k == 0 and nums[0] > 1:
        return 1
    elif k == 0 and nums[0] == 1:
        return -1
    elif k <= n - 1:
        if nums[k - 1] != nums[k]:
            return nums[k - 1]
        else:
            return -1
    elif k == n:
        return nums[k - 1]

        

main()