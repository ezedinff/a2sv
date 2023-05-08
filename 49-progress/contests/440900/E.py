'''
There are n kangaroos with pockets. Each kangaroo has a size (integer number). A kangaroo can go into another kangaroo's pocket if and only if the size of kangaroo who hold the kangaroo is at least twice as large as the size of kangaroo who is held.

Each kangaroo can hold at most one kangaroo, and the kangaroo who is held by another kangaroo cannot hold any kangaroos.

The kangaroo who is held by another kangaroo cannot be visible from outside. Please, find a plan of holding kangaroos with the minimal number of kangaroos who is visible.

Input
The first line contains a single integer — n (1 ≤ n ≤ 5·105). Each of the next n lines contains an integer si — the size of the i-th kangaroo (1 ≤ si ≤ 105).

Output
Output a single integer — the optimal number of visible kangaroos.

Examples
input
8
2
5
7
6
9
8
4
2
output
5

input
8
9
1
6
2
6
5
8
3
output
5

'''

def main():
    n = int(input())
    sizes = [int(input()) for _ in range(n)]
    sizes.sort()

    i = 0
    j = n // 2
    while j < n and i < n // 2:
        if sizes[j] >= 2 * sizes[i]:
            i += 1
        j += 1
    print(n - i)
main()


def main():
    n = int(input())
    sizes = [int(input()) for _ in range(n)]
    sizes.sort()
    
    # Precompute minimum size required to fit inside another kangaroo's pocket
    min_sizes = [sizes[i] * 2 for i in range(n)]
    for i in range(n-2, -1, -1):
        min_sizes[i] = min(min_sizes[i], min_sizes[i+1])
    
    # Use two pointers to iterate over sorted list
    i = 0
    j = n // 2
    while j < n and i < n // 2:
        # Use binary search to find smallest kangaroo that can fit current kangaroo
        if sizes[j] >= min_sizes[i]:
            i += 1
        j += 1
    print(n - i)

main()