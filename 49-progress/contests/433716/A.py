'''
A. Elevator
Rediet has arrived to the entrance of Abrehot and she wants to get to the 4th floor where the A2SV offices are. She would like to get to the office as fast as she can. She knows 𝑤𝑡
 how long it will take her to walk up a floor, 𝑒𝑡
 how long the elevator takes to travel between consecutive floors and 𝑒𝑓
, the floor that the elevator is on right now.

Armed with all this information, Rediet would like to know how long it will take her if she travels optimally.

Input
The first line will contain one integer 𝑡
 (1≤𝑡≤1000)
, the number of test cases. The next 𝑡
 lines will contain 3 integers 𝑤𝑡
 (1≤𝑤𝑡≤100)
, 𝑒𝑡
 (1≤𝑒𝑡≤100)
 and 𝑒𝑓
 (1≤𝑒𝑓≤4)
.

Output
For each of the test cases, output a single integer, the minimum time it'll take Rediet to get from floor 0 to floor 4.

Example
inputCopy
2
5 2 2
3 2 2
outputCopy
12
10
Note
For the first case, it's optimal if Rediet takes the elevator
 all the way up. So she takes 4 seconds waiting for the elevator
   to come to the ground floor and then 8 seconds riding it to floor 4.

For the second case, the optimal solution is to walk to floor 2 and then take the elevator up from there which takes a total of 6+4=10
.

'''    


def main():
    for _ in range(int(input())):
        wt, et, ef = map(int, input().split())
        ans = wt * 4
        if ef != 4:
            ans = min(ans, (4 - ef) * et + wt * 4)
        print(ans)
    


