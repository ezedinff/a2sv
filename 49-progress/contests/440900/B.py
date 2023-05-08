'''
After the lessons n groups of schoolchildren went outside and decided to visit
Polycarpus to celebrate his birthday. We know that the i-th group consists of
si friends (1 ≤ si ≤ 4), and they want to go to Polycarpus together.
They decided to get there by taxi. Each car can carry at most four passengers.
What minimum number of cars will the children need if all members of each group
should ride in the same taxi (but one taxi can take more than one group)?

Input
The first line contains integer n (1 ≤ n ≤ 105) — the number of groups of schoolchildren. The second line contains a sequence of integers s1, s2, ..., sn (1 ≤ si ≤ 4). The integers are separated by a space, si is the number of children in the i-th group.

Output
Print the single number — the minimum number of taxis necessary to drive all children to Polycarpus.

Examples
input
5
1 2 4 3 3
output
4
input
8
2 3 4 4 2 1 3 1
output
5
Note
In the first test we can sort the children into four cars like this:

the third group (consisting of four children),
the fourth group (consisting of three children),
the fifth group (consisting of three children),
the first and the second group (consisting of one and two children, correspondingly).
There are other ways to sort the groups into four cars.


'''

def main():
    n = int(input())
    groups = list(map(int, input().split()))
    d = {
        1: groups.count(1),
        2: groups.count(2),
        3: groups.count(3),
        4: groups.count(4)
    }
    taxis = d[4]
    taxis += d[3]
    if d[1] > d[3]:
        d[1] -= d[3]
    else:
        d[1] = 0
        
    taxis += d[2] // 2
    if d[2] % 2 == 1:
        taxis += 1
        if d[1] > 0:
            d[1] -= 2
        else:
            d[1] = 0
            
    taxis += (d[1] + 3) // 4
    print(taxis)

'''

The code first counts the number of groups of each size and stores it in a dictionary. Then, it fills up as many taxis as possible with the larger groups.

For example, if there are any groups of size 4, we can fill up a taxi with them. Similarly, if there are any groups of size 3, we can fill up a taxi with them.

Then, we handle the groups of size 1 and 2. If there are more groups of size 1 than size 3, we can use the remaining groups of size 1 to fill up taxis with the groups of size 2. Otherwise, we can ignore any remaining groups of size 1, since we can't use them to fill up a taxi with a group of size 2.

Finally, we count the number of taxis needed for the remaining groups of size 1. We use integer division and the modulus operator to determine how many taxis are needed for these groups.

Note that we need to add 3 before taking the ceiling of the division by 4, since we want to round up to the nearest multiple of 4.
'''