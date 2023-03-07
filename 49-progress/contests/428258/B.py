# https://codeforces.com/gym/428258/problem/B
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if len(set(a)) == 1:
        print(-1)
    else:
        print(*a)