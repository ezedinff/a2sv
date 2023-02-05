from collections import Counter


def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(solve(n, k, nums))

def solve(n, k, nums):
    nums.sort()
    for i in range(n - k + 1):
        if nums[i + k - 1] - nums[i] <= 1:
            return nums[i + k - 1]
    return -1

        

main()