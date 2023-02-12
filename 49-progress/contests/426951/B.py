# https://codeforces.com/gym/426951/problem/B

def main():
    n = int(input())
    cards = list(map(int, input().split()))
    sereja = 0
    dima = 0
    for i in range(n):
        if i % 2 == 0:
            if cards[0] > cards[-1]:
                sereja += cards[0]
                cards.pop(0)
            else:
                sereja += cards[-1]
                cards.pop(-1)
        else:
            if cards[0] > cards[-1]:
                dima += cards[0]
                cards.pop(0)
            else:
                dima += cards[-1]
                cards.pop(-1)
    print(sereja, dima)