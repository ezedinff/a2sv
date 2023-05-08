'''
Petya recieved a gift of a string s with length up to 105 characters for his birthday. He took two more empty strings t and u and decided to play a game. This game has two possible moves:

Extract the first character of s and append t with this character.
Extract the last character of t and append u with this character.
Petya wants to get strings s and t empty and string u lexicographically minimal.

You should write a program that will help Petya win the game.

Input
First line contains non-empty string s (1 ≤ |s| ≤ 105), consisting of lowercase English letters.

Output
Print resulting string u.

Examples
inputCopy
cab
outputCopy
abc
inputCopy
acdb
outputCopy
abdc

'''

# rewrite the above code in redable way and add comments
def main():
    s = input() # input string
    minimum_s = [chr(ord('z'))] * len(s) # minimum_s[i] is the minimum character in s[i:]
    minimum_s[-1] = s[-1]
    for i in range(len(s) - 2, -1, -1):
        minimum_s[i] = min(minimum_s[i + 1], s[i]) # minimum_s[i] = min(minimum_s[i + 1], s[i])
    t = [] # t is the stack of characters that are not yet appended to u
    u = [] # u is the string that is lexicographically minimal
    for i in range(len(s)):
        if len(t) == 0 or t[-1] <= minimum_s[i]: # if t is empty or the top of t is lexicographically smaller than minimum_s[i]
            while len(t) > 0 and t[-1] <= minimum_s[i]: # while t is not empty and the top of t is lexicographically smaller than minimum_s[i]
                u.append(t.pop()) # append the top of t to u
        if s[i] == minimum_s[i]: # if s[i] is the minimum character in s[i:]
            u.append(s[i]) # append s[i] to u
        else:
            t.append(s[i]) # append s[i] to t

    u += t[::-1] # append t in reverse order to u because t is a stack and we want to append the characters in the order they were pushed to t
    print(''.join(u))


# Define the main function
def main():
    # Get input string from user
    s = input()

    # Initialize a list of minimum characters to 'z' for each character in input string
    minimum_s = [chr(ord('z'))] * len(s)

    # Set the last character of minimum_s to the last character of input string
    minimum_s[-1] = s[-1]

    # Iterate over each character of input string in reverse order
    for i in range(len(s) - 2, -1, -1):
        # For each character, set minimum_s[i] to the minimum of minimum_s[i+1] and s[i]
        minimum_s[i] = min(minimum_s[i + 1], s[i])

    # Initialize an empty stack (t) and an empty string (u)
    t = []
    u = [] 

    # Iterate over each character of input string
    for i in range(len(s)):
        # If the stack is empty or the top of the stack is less than or equal to minimum_s[i],
        # keep popping elements from the stack and appending them to u until the top of the stack
        # is greater than minimum_s[i] or the stack becomes empty
        if len(t) == 0 or t[-1] <= minimum_s[i]:
            while len(t) > 0 and t[-1] <= minimum_s[i]:
                u.append(t.pop())

        # If s[i] is the minimum character in s[i:], append it to u
        if s[i] == minimum_s[i]:
            u.append(s[i])
        # Otherwise, push s[i] onto the stack
        else:
            t.append(s[i])
    
    # Append the remaining elements in the stack (t) to u in reverse order
    u += t[::-1]

    # Print the final string
    print(''.join(u))

# Call the main function
main()
