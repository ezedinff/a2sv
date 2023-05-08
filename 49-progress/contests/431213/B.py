'''
You are given a string 𝑠
 such that each its character is either 1, 2, or 3. You have to choose the shortest contiguous substring of 𝑠
 such that it contains each of these three characters at least once.

A contiguous substring of string 𝑠
 is a string that can be obtained from 𝑠
 by removing some (possibly zero) characters from the beginning of 𝑠
 and some (possibly zero) characters from the end of 𝑠
.

Input
The first line contains one integer 𝑡
 (1≤𝑡≤20000
) — the number of test cases.

Each test case consists of one line containing the string 𝑠
 (1≤|𝑠|≤200000
). It is guaranteed that each character of 𝑠
 is either 1, 2, or 3.

The sum of lengths of all strings in all test cases does not exceed 200000
.

Output
For each test case, print one integer — the length of the shortest contiguous substring of 𝑠
 containing all three types of characters at least once. If there is no such substring, print 0
 instead.

Example
inputCopy
7
123
12222133333332
112233
332211
12121212
333333
31121
outputCopy
3
3
4
4
0
0
4
Note
Consider the example test:

In the first test case, the substring 123 can be used.

In the second test case, the substring 213 can be used.

In the third test case, the substring 1223 can be used.

In the fourth test case, the substring 3221 can be used.

In the fifth test case, there is no character 3 in 𝑠
.

In the sixth test case, there is no character 1 in 𝑠
.

In the seventh test case, the substring 3112 can be used.


'''

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        s = input()
        print(solve(s))
def solve(s):
    if len(s) < 3:
        return 0
    if len(set(s)) < 3:
        return 0
    i = 0
    j = 0
    ans = float('inf')
    count = {}
    while j < len(s):
        count[s[j]] = count.get(s[j], 0) + 1
        while len(count) == 3:
            ans = min(ans, j - i + 1)
            count[s[i]] -= 1
            if count[s[i]] == 0:
                del count[s[i]]
            i += 1
        j += 1
    return ans
main()


'''
This problem requires finding the shortest contiguous substring of
a given string that contains all three characters 1, 2, and 3.

The input contains multiple test cases. For each test case, the first
line contains a single integer 𝑡, the number of test cases. Each of
the next 𝑡 lines contains a string 𝑠 consisting of characters 1, 2, or 3.

The output should contain 𝑡 lines. Each line should contain a single integer,
the length of the shortest contiguous substring of 𝑠 that contains all three
characters 1, 2, and 3. If there is no such substring, print 0 instead.

For example, consider the input:

7
123
12222133333332
112233
332211
12121212
333333
31121
For the first test case, the string 𝑠 is "123".
The shortest contiguous substring containing all three characters is "123",
which has length 3.

For the second test case, the string 𝑠 is "12222133333332".
The shortest contiguous substring containing all three characters is "2213333",
which has length 7.

For the fifth test case, the string 𝑠 is "12121212". There is no contiguous
substring of 𝑠 that contains all three characters, so the output is 0.
'''