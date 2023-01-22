'''
Your friend Mishka and you attend a calculus lecture. Lecture lasts 𝑛 minutes. Lecturer tells 𝑎𝑖 theorems during the 𝑖-th minute.

Mishka is really interested in calculus, though it is so hard to stay awake for all the time of lecture. You are given an array 𝑡 of Mishka's behavior. If Mishka is asleep during the 𝑖-th minute of the lecture then 𝑡𝑖 will be equal to 0, otherwise it will be equal to 1. When Mishka is awake he writes down all the theorems he is being told — 𝑎𝑖 during the 𝑖-th minute. Otherwise he writes nothing.

You know some secret technique to keep Mishka awake for 𝑘 minutes straight. However you can use it only once. You can start using it at the beginning of any minute between 1 and 𝑛−𝑘+1. If you use it on some minute 𝑖 then Mishka will be awake during minutes 𝑗 such that 𝑗∈[𝑖,𝑖+𝑘−1] and will write down all the theorems lecturer tells.

You task is to calculate the maximum number of theorems Mishka will be able to write down if you use your technique only once to wake him up.

Input
The first line of the input contains two integer numbers 𝑛 and 𝑘 (1≤𝑘≤𝑛≤105) — the duration of the lecture in minutes and the number of minutes you can keep Mishka awake.

The second line of the input contains 𝑛 integer numbers 𝑎1,𝑎2,…𝑎𝑛 (1≤𝑎𝑖≤104) — the number of theorems lecturer tells during the 𝑖-th minute.

The third line of the input contains 𝑛 integer numbers 𝑡1,𝑡2,…𝑡𝑛 (0≤𝑡𝑖≤1) — type of Mishka's behavior at the 𝑖-th minute of the lecture.

Output
Print only one integer — the maximum number of theorems Mishka will be able to write down if you use your technique only once to wake him up.

Example
input
6 3
1 3 5 2 5 4
1 1 0 1 0 0
output
16
Note
In the sample case the better way is to use the secret technique at the beginning of the third minute. Then the number of theorems Mishka will be able to write down will be equal to 16.
'''
'''
s = input().split()
time = int(s[1])
lec = input().split()
sleep = input().split()
def theorem(time, lec, sleep):
    tot=0
    # calculating theorem count
    for i in range(len(lec)):
        if sleep[i]=="1":
            tot+= int(lec[i])
 
    maxTot=tot
    temp=tot
    l=0
    for i in range(len(lec)):
        if sleep[i]=='0':
            temp += int(lec[i])
        if i>=time:
            if sleep[l]=='0':
                temp-= int(lec[l])
            l+=1
        maxTot= max(maxTot, temp)
    return maxTot
print(theorem(time, lec, sleep))
'''

def inputs():
    n, k = map(int, input().split()) # n is the number of minutes, k is the number of minutes you can keep Mishka awake
    a = list(map(int, input().split())) # a is the number of theorems lecturer tells during the ith minute
    t = list(map(int, input().split())) # t is the type of Mishka's behavior at the ith minute of the lecture
    return n, k, a, t

def main():
    n, k, a, t = inputs()
    ans = 0
    for i in range(len(a)):
        if t[i] == 1:
            ans += a[i]
    temp = ans
    l = 0
    for i in range(len(a)):
        if t[i] == 0:
            temp += a[i]
        if i >= k:
            if t[l] == 0:
                temp -= a[l]
            l += 1
        ans = max(ans, temp)
    print(ans)


if __name__ == '__main__':
    main()