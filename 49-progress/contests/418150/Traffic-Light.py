'''
This function first initializes the variables first_g, ans, and stack. Then, it iterates 
through the string s and adds the indices of all occurrences of the color c to the stack. 
If it encounters a green light, it pops all the indices from the stack and updates the minimum time. 
Finally, it pops all the remaining indices from the stack and updates the minimum time again.
'''
def findMinimumTime(n, c, s):
    if c == 'g':
        return 0
    first_g = -1
    ans = 0
    stack = []
    for i in range(n):
        if s[i] == c:
            stack.append(i)
        elif s[i] == 'g':
            if first_g == -1:
                first_g = i
            while len(stack) > 0:
                ans = max(ans, i - stack[-1])
                stack.pop()
    while len(stack) > 0:
        ans = max(ans, n - stack[-1] + first_g)
        stack.pop()
    return ans

def traffic_light():
    t = int(input())
    for i in range(t):
        n, c = input().split()
        n = int(n)
        s = input().strip()
        counter = findMinimumTime(n, c, s)
        print(counter)

traffic_light()









