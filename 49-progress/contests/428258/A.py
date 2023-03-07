'''
A. Min Unique Year
time limit per test1.0 s
memory limit per test64 MB
inputstandard input
outputstandard output
It seems like the year of 2013 came only yesterday. Do you know a curious fact? The year of 2013 is the first year after the old 1987 with only distinct digits.

Now you are suggested to solve the following problem: given a year number, find the minimum year number which is strictly larger than the given one and has only distinct digits.

Input
The single line contains integer 𝑦
 (1000≤𝑦≤9000)
 — the year number.

Output
Print a single integer — the minimum year number that is strictly larger than 𝑦
 and all it's digits are distinct. It is guaranteed that the answer exists.

Examples
input
1987
output
2013
input
2013
output
2014

'''

def main():
    y = int(input())
    while True:
        y += 1
        if len(set(str(y))) == len(str(y)):
            print(y)
            break
    