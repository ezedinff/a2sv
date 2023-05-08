'''
Vasya has a pile, that consists of some number of stones. 𝑛
 times he either took one stone from the pile or added one stone to the pile. The pile was non-empty before each operation of taking one stone from the pile.

You are given 𝑛
 operations which Vasya has made. Find the minimal possible number of stones that can be in the pile after making these operations.

Input
The first line contains one positive integer 𝑛
 — the number of operations, that have been made by Vasya (1≤𝑛≤100
).

The next line contains the string 𝑠
, consisting of 𝑛
 symbols, equal to "-" (without quotes) or "+" (without quotes). If Vasya took the stone on 𝑖
-th operation, 𝑠𝑖
 is equal to "-" (without quotes), if added, 𝑠𝑖
 is equal to "+" (without quotes).

Output
Print one integer — the minimal possible number of stones that can be in the pile after these 𝑛
 operations.

Examples
inputCopy
3
---
outputCopy
0
inputCopy
4
++++
outputCopy
4
inputCopy
2
-+
outputCopy
1
inputCopy
5
++-++
outputCopy
3
Note
In the first test, if Vasya had 3
 stones in the pile at the beginning, after making operations the number of stones will be equal to 0
. It is impossible to have less number of piles, so the answer is 0
. Please notice, that the number of stones at the beginning can't be less, than 3
, because in this case, Vasya won't be able to take a stone on some operation (the pile will be empty).

In the second test, if Vasya had 0
 stones in the pile at the beginning, after making operations the number of stones will be equal to 4
. It is impossible to have less number of piles because after making 4
 operations the number of stones in the pile increases on 4
 stones. So, the answer is 4
.

In the third test, if Vasya had 1
 stone in the pile at the beginning, after making operations the number of stones will be equal to 1
. It can be proved, that it is impossible to have less number of stones after making the operations.

In the fourth test, if Vasya had 0
 stones in the pile at the beginning, after making operations the number of stones will be equal to 3
.
'''

def main():
    n = int(input())
    s = input()
    ans = 0
    for c in s:
        if c == '+':
            ans += 1
        else:
            ans = max(0, ans - 1)
    print(ans)