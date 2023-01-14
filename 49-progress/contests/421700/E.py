'''
Vanya walks late at night along a straight street of length 𝑙, lit by 𝑛 lanterns. Consider the coordinate system with the beginning of the street corresponding to the point 0, and its end corresponding to the point 𝑙. Then the 𝑖-th lantern is at the point 𝑎𝑖. The lantern lights all points of the street that are at the distance of at most 𝑑 from it, where 𝑑 is some positive number, common for all lanterns.

Vanya wonders: what is the minimum light radius 𝑑 should the lanterns have to light the whole street?

Input
The first line contains two integers 𝑛, 𝑙 (1≤𝑛≤1000, 1≤𝑙≤109) — the number of lanterns and the length of the street respectively.

The next line contains 𝑛 integers 𝑎𝑖 (0≤𝑎𝑖≤𝑙). Multiple lanterns can be located at the same point. The lanterns may be located at the ends of the street.

Output
Print the minimum light radius 𝑑, needed to light the whole street. The answer will be considered correct if its absolute or relative error doesn't exceed 10−9.

Examples

input
7 15
15 5 3 7 9 14 0

output
2.5000000000


input
2 5
2 5

output
2.0000000000

Note
Consider the second sample. At 𝑑=2 the first lantern will light the segment [0,4] of the street, and the second lantern will light segment [3,5]. Thus, the whole street will be lit.
'''

def main():
    n, l = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    d = max(a[0], l - a[-1])
    for i in range(n - 1):
        d = max(d, (a[i + 1] - a[i]) / 2)
    print(f'{d:.10f}')
    

if __name__ == '__main__':
    main()