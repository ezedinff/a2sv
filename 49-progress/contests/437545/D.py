'''
D. Game 23
time limit per test3.0 s
memory limit per test500 MB
inputstandard input
outputstandard output
Polycarp plays "Game 23". Initially he has a number 𝑛
 and his goal is to transform it to 𝑚
. In one move, he can multiply 𝑛
 by 2
 or multiply 𝑛
 by 3
. He can perform any number of moves.

Print the number of moves needed to transform 𝑛
 to 𝑚
. Print -1 if it is impossible to do so.

It is easy to prove that any way to transform 𝑛
 to 𝑚
 contains the same number of moves (i.e. number of moves doesn't depend on the way of transformation).

Input
The only line of the input contains two integers 𝑛
 and 𝑚
 (1≤𝑛≤𝑚≤5⋅108
).

Output
Print the number of moves to transform 𝑛
 to 𝑚
, or -1 if there is no solution.

Examples
inputCopy
120 51840
outputCopy
7
inputCopy
42 42
outputCopy
0
inputCopy
48 72
outputCopy
-1
Note
In the first example, the possible sequence of moves is: 120→240→720→1440→4320→12960→25920→51840.
 The are 7
 steps in total.

In the second example, no moves are needed. Thus, the answer is 0
.

In the third example, it is impossible to transform 48
 to 72
.


'''

def main():
    # Read input values
    n, m = map(int, input().split())

    # Check if transformation is possible
    if m % n != 0:
        print(-1)
        return

    # Compute number of moves needed
    moves = 0
    m //= n
    while m % 2 == 0:
        m //= 2
        moves += 1
    while m % 3 == 0:
        m //= 3
        moves += 1
    if m != 1:
        print(-1)
        return

    # Print result
    print(moves)

# Call main function
main()
