'''
You are given 2 arrays representing the stock prices of a big tech company for 2 consecutive weeks, week1 and week2. 
A price is called k-repeating if the stock was sold for that price for k weeks consecutive weeks. 

Example: week1= [4,9,5,4], week2= [9,4,9,8,4]
ans = [4,9]
Prices 4 and 9 are 2-repeating because the stock has been sold for price 4 and price 9 in both weeks.
Return all 2-repeating prices. 

-> A price must appear in your result array as many times as it appears in its minimum appearance. 

week1= [4,4,9,5], week2= [9,4,9,8,4]
          p              [4, 4, 8, 9, 9]
res = [9, 4, 4]
d = {4: 1, 9: 0, 5: 0}
'''

# sort both nlogn
# two pointers i, j
# [4,4,5,9]  [4, 4, 8, 9, 9]
#  i          j
#  i == j => inc both and append value the result
#  i > j => inc j + 1
#  i < j => inc i + 1
# 

def solution2(week1, week2):
    # two pointer approach
    res = []
    week1 = sorted(week1) # nlogn
    week2 = sorted(week2) # mlogm
    i, j = 0, 0 # 
    while i < len(week1) and j < len(week2):
        if week1[i] == week2[j]:
            res.append(week1[i])
            i += 1
            j += 1
        elif week1[i] > week2[j]:
            j += 1
        else:
            i += 1
    return res
            

def solution(week1, week2):
    # solution using a dictionary
    res = []
    d = {} # O(n) -> space
    for i in week1: # O(n)
        if d.get(i, False):
            d[i] += 1
        else:
            d[i] = 1
    
    for i in week2: # O(m)
        if d.get(i, False):
            res.append(i)
            d[i] -= 1
    
    # O (n + m)
    return sorted(res)

A = []
B = []

res1 = solution(A,B)
res2 =  solution2(A,B)
assert(A == B)


