'''
Biruk's grandpa has a large collection of special stones. There is a legend that says one who has at least 5 unique special stones will be granted a wish by a higher power. Biruk's grandpa is sick. Help Biruk find out if his grandpa can be granted a wish.

Input
The first and only line of input contains the stones in grandpa's collection, where each stone is a lowercase latin letter ('a' to 'z').

Output
Print 'YES' if grandpa can be granted a wish. Otherwise, print NO.

Examples

input
a x a c d d
output
NO

input
d f g h f d s
output
YES

'''

stones = input()
stones = stones.split(' ')
stones = set(stones)

# all stones should be in lowercase a-z
if len(stones) >= 5 and all([ord(i) >= 97 and ord(i) <= 122 for i in stones]):
    print('YES')
else:
    print('NO')