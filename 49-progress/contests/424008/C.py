'''
C. How to Rearrange?
time limit per test1 s.
memory limit per test256 MB
inputstandard input
outputstandard output
You are given a string 𝑠
 consisting only of lowercase Latin letters.

You can rearrange all letters of this string as you wish. Your task is to obtain a good string by rearranging the letters of the given string or report that it is impossible to do it.

Let's call a string good if it is not a palindrome. Palindrome is a string which is read from left to right the same as from right to left. For example, strings "abacaba", "aa" and "z" are palindromes and strings "bba", "xd" are not.

You have to answer 𝑡
 independent queries.

Input
The first line of the input contains one integer 𝑡
 (1≤𝑡≤100
) — number of queries.

Each of the next 𝑡
 lines contains one string. The 𝑖
-th line contains a string 𝑠𝑖
 consisting only of lowercase Latin letter. It is guaranteed that the length of 𝑠𝑖
 is from 1
 to 1000
 (inclusive).

Output
Print 𝑡
 lines. In the 𝑖-th line print the answer to the 𝑖-th query: -1 if it is impossible to obtain a good string by rearranging the letters of 𝑠𝑖
 and any good string which can be obtained from the given one (by rearranging the letters) otherwise.

Example
input
3
aa
abacaba
xdd
output
-1
abaacba
xdd
'''

from typing import List
import unittest

def get_inputs() -> List[str]:
    t = int(input())
    res = []
    for _ in range(t):
        s = input()
        res.append(s)
    return res

def main():
    inputs = get_inputs()
    for s in inputs:
        print(canRearrange(s))


def canRearrange(s: str) -> str:
    if len(set(s)) == 1:
        return '-1'
    elif s != s[::-1]:
        return s
    else:
        return s[0] + s[2:] + s[1]



class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(canRearrange('aa'), '-1')

    def test2(self):
        self.assertEqual(canRearrange('abacaba'), 'abaacba')

    def test3(self):
        self.assertEqual(canRearrange('xdd'), 'xdd')


if __name__ == '__main__':
    unittest.main()