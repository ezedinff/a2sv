# https://codeforces.com/gym/426951/problem/A
def main():
    testCases = int(input())
    for _ in range(testCases):
        n = int(input())
        sequence = list(map(int, input().split()))
        print(' '.join(map(str, solve(sequence))))

def solve(sequence):
    result = []
    while len(sequence) > 0:
        if len(sequence) == 1:
            result.append(sequence.pop())
        else:
            result.append(sequence.pop(0))
            result.append(sequence.pop())
    return result