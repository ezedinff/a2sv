'''
You are given a string 𝑠[1…𝑛]
 consisting of lowercase Latin letters. It is guaranteed that 𝑛=2𝑘
 for some integer 𝑘≥0
.

The string 𝑠[1…𝑛]
 is called 𝑐
-good if at least one of the following three conditions is satisfied:

The length of 𝑠
 is 1
, and it consists of the character 𝑐
 (i.e. 𝑠1=𝑐
);
The length of 𝑠
 is greater than 1
, the first half of the string consists of only the character 𝑐
 (i.e. 𝑠1=𝑠2=⋯=𝑠𝑛2=𝑐
) and the second half of the string (i.e. the string 𝑠𝑛2+1𝑠𝑛2+2…𝑠𝑛
) is a (𝑐+1)
-good string;
The length of 𝑠
 is greater than 1
, the second half of the string consists of only the character 𝑐
 (i.e. 𝑠𝑛2+1=𝑠𝑛2+2=⋯=𝑠𝑛=𝑐
) and the first half of the string (i.e. the string 𝑠1𝑠2…𝑠𝑛2
) is a (𝑐+1)
-good string.
For example: "aabc" is 'a'-good, "ffgheeee" is 'e'-good.

In one move, you can choose one index 𝑖
 from 1
 to 𝑛
 and replace 𝑠𝑖
 with any lowercase Latin letter (any character from 'a' to 'z').

Your task is to find the minimum number of moves required to obtain an 'a'-good string from 𝑠
 (i.e. 𝑐
-good string for 𝑐=
 'a'). It is guaranteed that the answer always exists.

You have to answer 𝑡
 independent test cases.

Another example of an 'a'-good string is as follows. Consider the string 𝑠=
"cdbbaaaa". It is an 'a'-good string, because:

the second half of the string ("aaaa") consists of only the character 'a';
the first half of the string ("cdbb") is 'b'-good string, because:
the second half of the string ("bb") consists of only the character 'b';
the first half of the string ("cd") is 'c'-good string, because:
the first half of the string ("c") consists of only the character 'c';
the second half of the string ("d") is 'd'-good string.
Input
The first line of the input contains one integer 𝑡
 (1≤𝑡≤2⋅104
) — the number of test cases. Then 𝑡
 test cases follow.

The first line of the test case contains one integer 𝑛
 (1≤𝑛≤131 072
) — the length of 𝑠
. It is guaranteed that 𝑛=2𝑘
 for some integer 𝑘≥0
. The second line of the test case contains the string 𝑠
 consisting of 𝑛
 lowercase Latin letters.

It is guaranteed that the sum of 𝑛
 does not exceed 2⋅105
 (∑𝑛≤2⋅105
).

Output
For each test case, print the answer — the minimum number of moves required to obtain an 'a'-good string from 𝑠
 (i.e. 𝑐
-good string with 𝑐=
 'a'). It is guaranteed that the answer exists.

Example
inputCopy
6
8
bbdcaaaa
8
asdfghjk
8
ceaaaabb
8
bbaaddcc
1
z
2
ac
outputCopy
0
7
4
5
1
1

'''

# Define a function called 'ans' that takes in two arguments: a string 's' and a character 'c'
def ans(s, c):
    
    # Get the length of the string
    n = len(s)
    
    # If the string is only one character long, return 1 if it is not equal to 'c' (as an integer)
    if n == 1:
        return int(ord(s[0]) != c)
    
    # Divide the string in half
    n //= 2
    
    # Recursively call the 'ans' function on each half of the string, incrementing 'c' by 1 each time
    left_half = ans(s[:n], c+1)
    right_half = ans(s[n:], c+1)
    
    # Count the number of occurrences of 'c' in each half of the string and subtract from the length of the other half
    left_count = n - s[n:].count(chr(c))
    right_count = n - s[:n].count(chr(c))
    
    # Return the minimum of the sum of each half's count and the result of the recursive call on the other half
    return min(left_half + left_count, right_half + right_count)


# Loop over a range of inputs (specified by the user) and run the 'ans' function on each input string
for _ in range(int(input())):
    input() # Discard this input (not used in the 'ans' function)
    print(ans(input(), 97)) # Run 'ans' on the user's input and print the result



def main():
    for _ in range(int(input())):
        n = int(input())
        c = 97
        if n == 1:
            print(ord(input()) != c)
        else:
            n //= 2
            s = input()
            left_half = ans(s[:n], c+1)
            right_half = ans(s[n:], c+1)
            left_count = n - s[n:].count(chr(c))
            right_count = n - s[:n].count(chr(c))
            print(min(left_half + left_count, right_half + right_count))
