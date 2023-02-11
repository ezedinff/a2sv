# https://codeforces.com/contest/1343/problem/C

def alternatingSubsequence(a):
    n = len(a)
    if n == 1:
        return a[0]
    max_sum = 0
    i = 0
    while i < n:
        j = i + 1
        while j < n and a[j] * a[i] > 0:
            j += 1
        max_sum += max(a[i:j])
        i = j
    return max_sum


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(alternatingSubsequence(a))