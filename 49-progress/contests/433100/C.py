'''
Yohannes can convert an integer into the sum of its digits in one step. How many steps does it take him to convert a given number to a one-digit number?

Input
The input contains one non-negative integer 𝑛
 (≤10100000
) with no leading zeroes.

Output
Print the number of steps.

Examples
inputCopy
0
outputCopy
0
inputCopy
10
outputCopy
1
inputCopy
991
outputCopy
3
Note
In the third test, the number 991 undergoes a series of transformations
which are as follows: 991 transforms into 19, then into 10, and finally into 1.
As a result of these three transformations,the number ends up becoming a single-digit number.
'''

def main():
    n = input()
    count = 0
    while len(n) > 1:
        count += 1
        n = str(sum(map(int, n)))
    print(count)