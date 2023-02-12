# check if there is exactly one valley in the list
'''
input:
6
7
3 2 2 1 2 2 3
11
1 1 1 2 3 3 4 5 6 6 6
7
1 2 3 4 3 2 1
7
9 7 4 6 9 9 10
1
1000000000
8
9 4 4 5 9 4 9 10

output:
YES
YES
NO
YES
YES
NO
'''
def main():
    test_cases = int(input())
    for _ in range(test_cases):
        n = int(input())
        a = list(map(int, input().split()))
        print('YES' if no_of_valleys(n, a) == 1 else 'NO')

def no_of_valleys(n, a) -> int:
    valleys = 0
    left = right = 0
    while right < n:
        while right + 1 < n and a[right] >= a[right + 1]:
            right += 1
        if left == 0 or a[left - 1] > a[left]:
            if right == n - 1 or a[right] < a[right + 1]:
                valleys += 1
        right += 1
        left = right
    return valleys
