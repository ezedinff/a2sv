'''
https://www.hackerrank.com/challenges/making-candies/problem

sample input: 3 1 2 12
sample output: 3

sample input: 1 1 6 45
sample output: 16
'''
from math import ceil


def minimumPasses(m, w, p, n):
    days = 0
    candies = 0
    answer = ceil(n / (m * w))
    while days < answer:
        if p > candies:
            daysNeeded = ceil((p - candies) / (m * w))
            candies += daysNeeded * m * w
            days += daysNeeded
        diff = abs(m - w)
        available = candies // p
        purchased = min(available, diff)
        if m > w:
            w += purchased
        else:
            m += purchased
       
        rest = available - purchased
        m += rest // 2
        w += rest - rest // 2
        candies -= available * p

        candies += m * w
        days += 1

        answer = min(answer, days + ceil((n - candies) / (m * w)))

    return answer


if __name__ == "__main__":
    m, w, p, n = input().strip().split(' ')
    m, w, p, n = [int(m), int(w), int(p), int(n)]
    result = minimumPasses(m, w, p, n)
    print(result)