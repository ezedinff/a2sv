'''
The next A2SV camp is going to be held in a larger class in order to teach 𝑛
 students. The only problem is that this class has only 2
 power outlets and every student needs one outlet to plug in their computer. In order to solve this problem, Miruts has brought 𝑚
 dividers, where the 𝑖
-𝑡ℎ
 divider plugs into one power outlet and creates 𝑎𝑖
 additional outlets.

Find the minimum number of dividers so that each student gets one power outlet.

Input
The first line contains a single integer 𝑡
 (1≤𝑡≤103)
 — the number of test cases.

The first line of each test case contains two integers, 𝑛
 (1≤𝑛≤107)
 and 𝑚
 (0≤𝑚≤105)
, the number of students and the number of power outlets respectively. The next line will contain a space separated integer array 𝑎
 of size 𝑚
, where 𝑎𝑖
 (1≤𝑎𝑖≤102)
 shows the outlets created by the 𝑖
-𝑡ℎ
 divider.

The sum of all 𝑚
 across a test case won't exceed 2∗105
Output
For each test case, print out the minimum number of dividers needed to provide enough outlets for all students. If it is impossible, print out -1.

Examples
inputCopy
1
7 4
2 4 2 2
outputCopy
3
inputCopy
2
1 1
9
2 3
2 3 2
outputCopy
0
0
Note
For the first example, we would use the 4-outlet divider and 2 of the 2-outlet dividers to have a total of 5 free outlets for the students to use.
'''
def main():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        a.sort(reverse=True)
        if m == 0:
            print(-1)
            continue
        if a[0] == 1:
            print(-1)
            continue
        ans = 0
        while n > 0:
            ans += 1
            n -= a[0] - 1
            a[0] = 1
            a.sort(reverse=True)
        print(ans)
main()