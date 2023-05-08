'''
Kuriyama Mirai has killed many monsters and got many (namely n) stones. She numbers the stones from 1 to n. The cost of the i-th stone is vi. Kuriyama Mirai wants to know something about these stones so she will ask you two kinds of questions:

She will tell you two numbers, l and r (1 ≤ l ≤ r ≤ n), and you should tell her .
Let ui be the cost of the i-th cheapest stone (the cost that will be on the i-th place if we arrange all the stone costs in non-decreasing order). This time she will tell you two numbers, l and r (1 ≤ l ≤ r ≤ n), and you should tell her .
For every question you should give the correct answer, or Kuriyama Mirai will say "fuyukai desu" and then become unhappy.

Input
The first line contains an integer n (1 ≤ n ≤ 105). The second line contains n integers: v1, v2, ..., vn (1 ≤ vi ≤ 109) — costs of the stones.

The third line contains an integer m (1 ≤ m ≤ 105) — the number of Kuriyama Mirai's questions. Then follow m lines, each line contains three integers type, l and r (1 ≤ l ≤ r ≤ n; 1 ≤ type ≤ 2), describing a question. If type equal to 1, then you should output the answer for the first question, else you should output the answer for the second one.

Output
Print m lines. Each line must contain an integer — the answer to Kuriyama Mirai's question. Print the answers to the questions in the order of input.

Examples
inputCopy
6
6 4 2 7 2 7
3
2 3 6
1 3 4
1 1 6
outputCopy
24
9
28
inputCopy
4
5 5 2 3
10
1 2 4
2 1 4
1 1 1
2 1 4
2 1 2
1 1 1
1 3 3
1 1 3
1 4 4
1 2 2
outputCopy
10
15
5
15
5
5
2
12
3
5
Note
Please note that the answers to the questions may overflow 32-bit integer type.
'''

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    c = [0] * n
    d = [0] * n
    c[0] = a[0]
    d[0] = b[0]
    for i in range(1, n):
        c[i] = a[i] + c[i - 1]
        d[i] = b[i] + d[i - 1]
    m = int(input())
    for i in range(m):
        t, l, r = map(int, input().split())
        l -= 1
        r -= 1
        if t == 1:
            print(c[r] - c[l] + a[l])
        else:
            print(d[r] - d[l] + b[l])


'''
The problem requires you to process two types of queries on an array of numbers.
The array represents the cost of stones where the cost of the i-th stone is vi.

The first type of query requires you to calculate the sum of costs of stones between
indices l and r (inclusive) of the original array.

The second type of query requires you to calculate the sum of costs of stones between
indices l and r (inclusive) of the sorted array.

You are given the number of stones n, the cost of each stone, the number of queries m,
 and the queries in the form of type, l, and r.

For each query, you need to output the answer on a separate line.

The problem guarantees that the answers will not overflow the 32-bit integer type.

'''