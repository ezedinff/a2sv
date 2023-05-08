'''
You are given 4𝑛
 sticks, the length of the 𝑖
-th stick is 𝑎𝑖
.

You have to create 𝑛
 rectangles, each rectangle will consist of exactly 4
 sticks from the given set. The rectangle consists of four sides, opposite sides should have equal length and all angles in it should be right. Note that each stick can be used in only one rectangle. Each stick should be used as a side, you cannot break the stick or use it not to the full length.

You want to all rectangles to have equal area. The area of the rectangle with sides 𝑎
 and 𝑏
 is 𝑎⋅𝑏
.

Your task is to say if it is possible to create exactly 𝑛
 rectangles of equal area or not.

You have to answer 𝑞
 independent queries.

Input
The first line of the input contains one integer 𝑞
 (1≤𝑞≤500
) — the number of queries. Then 𝑞
 queries follow.

The first line of the query contains one integer 𝑛
 (1≤𝑛≤100
) — the number of rectangles.

The second line of the query contains 4𝑛
 integers 𝑎1,𝑎2,…,𝑎4𝑛
 (1≤𝑎𝑖≤104
), where 𝑎𝑖
 is the length of the 𝑖
-th stick.

Output
For each query print the answer to it. If it is impossible to create exactly 𝑛
 rectangles of equal area using given sticks, print "NO". Otherwise print "YES".

Example
inputCopy
5
1
1 1 10 10
2
10 5 2 10 1 1 2 5
2
10 5 1 10 5 1 1 1
2
1 1 1 1 1 1 1 1
1
10000 10000 10000 10000
outputCopy
YES
YES
NO
YES
YES

'''

def main():
    for _ in range(int(input())):
        n = int(input())
        sticks = sorted(list(map(int, input().split()))[:4*n])
        
        is_possible = True
        area = sticks[0] * sticks[-1] # w * h
        
        for i in range(0, 4*n-1, 2):
            if sticks[i] != sticks[i+1] or sticks[i]*sticks[-1-i] != area:
                is_possible = False
                break
                
        if is_possible:
            print("YES")
        else:
            print("NO")


main()
