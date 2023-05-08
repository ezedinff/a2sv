'''
Sereja and Dima play a game. The rules of the game are very simple. The players have n cards in a row. Each card contains a number, all numbers on the cards are distinct. The players take turns, Sereja moves first. During his turn a player can take one card: either the leftmost card in a row, or the rightmost one. The game ends when there is no more cards. The player who has the maximum sum of numbers on his cards by the end of the game, wins.

Sereja and Dima are being greedy. Each of them chooses the card with the larger number during his move.

Inna is a friend of Sereja and Dima. She knows which strategy the guys are using, so she wants to determine the final score, given the initial state of the game. Help her.

Input
The first line contains integer n (1 ≤ n ≤ 1000) — the number of cards on the table. The second line contains space-separated numbers on the cards from left to right. The numbers on the cards are distinct integers from 1 to 1000.

Output
On a single line, print two integers. The first number is the number of Sereja's points at the end of the game, the second number is the number of Dima's points at the end of the game.

Examples
inputCopy
4
4 1 2 10
outputCopy
12 5
inputCopy
7
1 2 3 4 5 6 7
outputCopy
16 12
Note
In the first sample Sereja will take cards with numbers 10 and 2, so Sereja's sum is 12. Dima will take cards with numbers 4 and 1, so Dima's sum is 5.
'''

def main():
    n = int(input())
    cards = list(map(int, input().split()))
    sereja = 0
    dima = 0
    for i in range(n):
        if i % 2 == 0:
            sereja += max(cards[0], cards[-1])
            if cards[0] > cards[-1]:
                cards.pop(0)
            else:
                cards.pop()
        else:
            dima += max(cards[0], cards[-1])
            if cards[0] > cards[-1]:
                cards.pop(0)
            else:
                cards.pop()
    print(sereja, dima)
    
main()


'''
The problem describes a game played by Sereja and Dima.
The game is played with a row of n cards, each card containing
a distinct number. The players take turns to choose a card from
either the leftmost or rightmost end of the row. The player who chooses
the card with the higher number adds the number to their score.
The game ends when there are no more cards to choose from.

The objective of the problem is to calculate the final score of both
players given the initial state of the game and their strategy of choosing
the card with the higher number during their turn.

The input consists of two lines. The first line contains an integer n, representing
the number of cards on the table. The second line contains n space-separated 
integers representing the distinct numbers on the cards from left to right.

The output should be a single line containing two integers separated by
a space, representing the final score of Sereja and Dima, respectively.
'''