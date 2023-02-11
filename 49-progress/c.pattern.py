# https://codeforces.com/problemset/problem/412/C
def solve(n, patterns):
    ans = []
    for i in range(len(patterns[0])):
        chars = set()
        for pattern in patterns:
            if pattern[i] != '?':
                chars.add(pattern[i])
        if len(chars) == 1:
            ans.append(chars.pop())
        elif len(chars) > 1:
            ans.append('?')
        else:
            ans.append('x')
    return ''.join(ans)


n = int(input())
patterns = [input() for _ in range(n)]
print(solve(n, patterns))