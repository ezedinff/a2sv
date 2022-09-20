'''
https://www.hackerrank.com/challenges/crush/problem
'''

def arrayManipulation(n, queries):
    arr = [0] * (n+1)
    for a, b, k in queries:
        arr[a-1] += k
        arr[b] -= k
    max_val = 0
    curr = 0
    for i in arr:
        curr += i
        max_val = max(max_val, curr)
    return max_val

if __name__ == '__main__':
    n, m = map(int, input().split())
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().split())))
    print(arrayManipulation(n, queries))