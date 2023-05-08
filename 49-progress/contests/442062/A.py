'''
Pak Chanek has a prime number†
 𝑛
. Find a prime number 𝑚
 such that 𝑛+𝑚
 is not prime.

†
 A prime number is a number with exactly 2
 factors. The first few prime numbers are 2,3,5,7,11,13,…
. In particular, 1
 is not a prime number.

Input
Each test contains multiple test cases. The first line contains an integer 𝑡
 (1≤𝑡≤104
) — the number of test cases. The following lines contain the description of each test case.

The only line of each test case contains a prime number 𝑛
 (2≤𝑛≤105
).

Output
For each test case, output a line containing a prime number 𝑚
 (2≤𝑚≤105
) such that 𝑛+𝑚
 is not prime. It can be proven that under the constraints of the problem, such 𝑚
 always exists.

If there are multiple solutions, you can output any of them.

Example
inputCopy
3
7
2
75619
outputCopy
2
7
47837
Note
In the first test case, 𝑚=2
, which is prime, and 𝑛+𝑚=7+2=9
, which is not prime.

In the second test case, 𝑚=7
, which is prime, and 𝑛+𝑚=2+7=9
, which is not prime.

In the third test case, 𝑚=47837
, which is prime, and 𝑛+𝑚=75619+47837=123456
, which is not prime.
'''

for _ in range(int(input())):
    n = int(input())
    print(n)





        
