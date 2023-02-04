'''
C. Largest Segment
time limit per test2 s.
memory limit per test256 MB
inputstandard input
outputstandard output
A coordinate line has 𝑛
 segments, the 𝑖
-th segment starts at the position 𝑙𝑖
 and ends at the position 𝑟𝑖
. We will denote such a segment as [𝑙𝑖,𝑟𝑖]
.

You have suggested that one of the defined segments covers all others. In other words, there is such segment in the given set, which contains all other ones. Now you want to test your assumption. Find in the given set the segment which covers all other segments, and print its number. If such a segment doesn't exist, print -1.

Formally we will assume that segment [𝑎,𝑏]
 covers segment [𝑐,𝑑]
, if they meet this condition 𝑎≤𝑐≤𝑑≤𝑏
.

Input
The first line contains integer 𝑛
 (1≤𝑛≤105
) — the number of segments. Next 𝑛
 lines contain the descriptions of the segments. The 𝑖
-th line contains two space-separated integers 𝑙𝑖,𝑟𝑖
 (1≤𝑙𝑖≤𝑟𝑖≤109
) — the borders of the 𝑖
-th segment.

It is guaranteed that no two segments coincide.

Output
Print a single integer — the number of the segment that covers all other segments in the set. If there's no solution, print -1.

The segments are numbered starting from 1
 in the order in which they appear in the input.

Examples
inputCopy
3
1 1
2 2
3 3
outputCopy
-1
inputCopy
6
1 5
2 3
1 10
7 10
7 7
10 10
outputCopy
3

'''
def main():
    n = int(input().strip())
    min_r = float('inf')
    max_l = float('-inf')
    max_r = float('-inf')
    segment = -1
    for i in range(n):
        l, r = map(int, input().strip().split())
        if l <= min_r and r >= max_r:
            segment = i + 1
            min_r = min(min_r, r)
            max_l = max(max_l, l)
            max_r = max(max_r, r)
    if segment == 1:
        print(segment * -1)
        return
    if min_r >= max_l:
        print(segment)
    else:
        print(-1)

if __name__ == '__main__':
    main()
