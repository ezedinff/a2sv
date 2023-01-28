'''
A. Compare Strings
time limit per test1.0 s
memory limit per test256 MB
inputstandard input
outputstandard output
Little Petya loves presents. His mum bought him two strings of the same size for his birthday. The strings consist of uppercase and lowercase Latin letters.
Now Petya wants to compare those two strings lexicographically. The letters' case does not matter, that is an uppercase letter is considered equivalent to the corresponding lowercase letter.
Help Petya perform the comparison.

Input
Each of the first two lines contains a bought string. The strings' lengths range from 1 to 100
inclusive. It is guaranteed that the strings are of the same length and also consist of uppercase and lowercase Latin letters.

Output
If the first string is less than the second one, print "-1". If the second string is less than the first one, print "1". If the strings are equal, print "0".
Note that the letters' case is not taken into consideration when the strings are compared.
input
aaaa
aaaA
output
0

'''

from typing import List

def compareStrings(s1: str, s2: str) -> int:
    return (s1.lower() > s2.lower()) - (s1.lower() < s2.lower())

def get_inputs() -> List[str]:
    s1 = input()
    s2 = input()
    return [s1, s2]

def main():
    s1, s2 = get_inputs()
    print(compareStrings(s1, s2))

if __name__ == '__main__':
    main()