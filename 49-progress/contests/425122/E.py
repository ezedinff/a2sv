'''
E. N Events
time limit per test3.0 s
memory limit per test256 MB
inputstandard input
outputstandard output
Polycarpus likes studying at school a lot and he is always diligent about his homework. Polycarpus has never had any problems with natural sciences as his great-great-grandfather was the great physicist Seinstein. On the other hand though, Polycarpus has never had an easy time with history.

Everybody knows that the World history encompasses exactly 𝑛
 events: the 𝑖
-th event had continued from the year 𝑎𝑖
 to the year 𝑏𝑖
 inclusive (𝑎𝑖<𝑏𝑖
). Polycarpus easily learned the dates when each of 𝑛
 events started and ended (Polycarpus inherited excellent memory from his great-great-granddad). But the teacher gave him a more complicated task: Polycaprus should know when all events began and ended and he should also find out for each event whether it includes another event. Polycarpus' teacher thinks that an event 𝑗
 includes an event 𝑖
 if 𝑎𝑗<𝑎𝑖
 and 𝑏𝑖<𝑏𝑗
. Your task is simpler: find the number of events that are included in some other event.

Input
The first input line contains integer 𝑛
 (1≤𝑛≤105
) which represents the number of events. Next 𝑛
 lines contain descriptions of the historical events, one event per line. The 𝑖+1
 line contains two integers 𝑎𝑖
 and 𝑏𝑖
 (1≤𝑎𝑖<𝑏𝑖≤109
) — the beginning and the end of the 𝑖
-th event. No two events start or finish in the same year, that is, 𝑎𝑖≠𝑎𝑗,𝑎𝑖≠𝑏𝑗,𝑏𝑖≠𝑎𝑗,𝑏𝑖≠𝑏𝑗
 for all 𝑖
, 𝑗
 (where 𝑖≠𝑗
). Events are given in arbitrary order.

Output
Print the only integer — the answer to the problem.

Examples
input
5
1 10
2 9
3 8
4 7
5 6
output
4


input
5
1 100
2 50
51 99
52 98
10 60
output
4


input
1
1 1000000000
output
0


Note
In the first example the fifth event is contained in the fourth. Similarly, the fourth event is contained in the third, the third — in the second and the second — in the first.

In the second example all events except the first one are contained in the first.

In the third example only one event, so the answer is 0.
'''

'''
this should pass
input
5
1 100
2 50
51 99
52 98
10 60
output
4
'''
def main():
    n = int(input())
    events = []
    for _ in range(n):
        a, b = map(int, input().strip().split())
        events.append((a, b))

    if len(events) == 1:
        print(0)

    events.sort(key=lambda x: x[0])
    ans = 0
    for i in range(1, n):
        if(events[i][0] <= events[i - 1][1] or events[i][0] > events[i - 1][1]):
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
    
    