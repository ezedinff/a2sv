'''
Kirito is stuck on a level of the MMORPG he is playing now. To move on in the game, he's got to defeat all 𝑛
 dragons that live on this level. Kirito and the dragons have strength, which is represented by an integer. In the duel between two opponents the duel's outcome is determined by their strength. Initially, Kirito's strength equals 𝑠
.

If Kirito starts duelling with the 𝑖
-th (1≤𝑖≤𝑛
) dragon and Kirito's strength is not greater than the dragon's strength 𝑥𝑖
, then Kirito loses the duel and dies. But if Kirito's strength is greater than the dragon's strength, then he defeats the dragon and gets a bonus strength increase by 𝑦𝑖
.

Kirito can fight the dragons in any order. Determine whether he can move on to the next level of the game, that is, defeat all dragons without a single loss.

Input
The first line contains two space-separated integers 𝑠
 and 𝑛
 (1≤𝑠≤104
, 1≤𝑛≤103
). Then 𝑛
 lines follow: the 𝑖
-th line contains space-separated integers 𝑥𝑖
 and 𝑦𝑖
 (1≤𝑥𝑖≤104
, 0≤𝑦𝑖≤104
) — the 𝑖
-th dragon's strength and the bonus for defeating it.

Output
On a single line print "YES" (without the quotes), if Kirito can move on to the next level and print "NO" (without the quotes), if he can't.

Examples
inputCopy
2 2
1 99
100 0
output
YES

input
10 1
100 100
output
NO
'''

from typing import List

def canDefeatDragons(s: int, dragons: List[List[int]]) -> bool:
    dragons.sort(key=lambda x: x[0])
    for x, y in dragons:
        if s <= x:
            return False
        s += y
    return True

# why sort the dragons by their strength?
# because if we fight the dragons in order of their strength, we will always have enough strength to defeat them

def get_inputs() -> List[int]:
    s, n = map(int, input().split())
    dragons = [list(map(int, input().split())) for _ in range(n)]
    return [s, dragons]

def main():
    s, dragons = get_inputs()
    print('YES' if canDefeatDragons(s, dragons) else 'NO')

main()  