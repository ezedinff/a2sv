# https://codeforces.com/gym/426951/problem/E
t = int(input())
for _ in range(t):
    n, c = input().split()
    n = int(n)
    s = input()
    if c == 'g': print(0); continue

    nxt = 0
    for p in range(len(s)):
        if s[p] == 'g':
            nxt = n + p
            break

    res = 0
    for p in range(n - 1, -1, -1):
        if s[p] == 'g':
            nxt = p
        elif s[p] == c:
            cur = nxt - p
            res = max(res, cur)

    print(res)

