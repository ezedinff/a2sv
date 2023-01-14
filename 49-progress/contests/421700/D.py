'''
Vasya has recently learned to type and log on to the Internet. He immediately entered a chat room and decided to say hello to everybody. Vasya typed the word 𝑠. It is considered that Vasya managed to say hello if several letters can be deleted from the typed word so that it resulted in the word "hello". For example, if Vasya types the word "ahhellllloou", it will be considered that he said hello, and if he types "hlelo", it will be considered that Vasya got misunderstood and he didn't manage to say hello. Determine whether Vasya managed to say hello by the given word 𝑠.

Input
The first and only line contains the word 𝑠, which Vasya typed. This word consisits of small Latin letters, its length is no less that 1 and no more than 100 letters.

Output
If Vasya managed to say hello, print "YES", otherwise print "NO".

Examples
input
ahhellllloou

output
YES


input
hlelo

output
NO
'''

def main():
    s = input()
    hello = 'hello'
    i = 0
    for c in s:
        if c == hello[i]:
            i += 1
            if i == 5:
                break
    print('YES' if i == 5 else 'NO')

if __name__ == '__main__':
    main()