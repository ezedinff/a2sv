'''
input
4
18 55 16 17
output
YES

input
6
40 41 43 44 44 44

output
NO

input
8
5 972 3 4 1 4 970 971

output
YES

'''

def solve(balls):
    if len(balls) < 3:
        return 'NO'
    for ball in balls:
        if ball - 1 in balls and ball + 1 in balls:
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    n = int(input())
    balls = set(map(int, input().split()))
    print(solve(balls))
