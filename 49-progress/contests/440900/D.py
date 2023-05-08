'''
Being a programmer, you like arrays a lot. For your birthday, your friends have given you an array a consisting of n distinct integers.

Unfortunately, the size of a is too small. You want a bigger array! Your friends agree to give you a bigger array, but only if you are able to answer the following question correctly: is it possible to sort the array a (in increasing order) by reversing exactly one segment of a? See definitions of segment and reversing in the notes.

Input
The first line of the input contains an integer n (1 ≤ n ≤ 105) — the size of array a.

The second line contains n distinct space-separated integers: a[1], a[2], ..., a[n] (1 ≤ a[i] ≤ 109).

Output
Print "yes" or "no" (without quotes), depending on the answer.

If your answer is "yes", then also print two space-separated integers denoting start and end (start must not be greater than end) indices of the segment to be reversed. If there are multiple ways of selecting these indices, print any of them.

Examples
input
3
3 2 1
output
yes
1 3

input
4
2 1 3 4
output
yes
1 2

input
4
3 1 2 4
output
no

input
2
1 2
output
yes
1 1

Note
Sample 1. You can reverse the entire array to get [1, 2, 3], which is sorted.

Sample 3. No segment can be reversed such that the array will be sorted.

Definitions

A segment [l, r] of array a is the sequence a[l], a[l + 1], ..., a[r].

If you have an array a of size n and you reverse its segment [l, r], the array will become:

a[1], a[2], ..., a[l - 2], a[l - 1], a[r], a[r - 1], ..., a[l + 1], a[l], a[r + 1], a[r + 2], ..., a[n - 1], a[n].
'''

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    start = 0
    end = 0
    for i in range(n):
        if a[i] != b[i]:
            start = i
            break
    for i in range(n - 1, -1, -1):
        if a[i] != b[i]:
            end = i
            break
    if a[start:end + 1] == b[start:end + 1][::-1]:
        print('yes')
        print(start + 1, end + 1)
    else:
        print('no')
main()

