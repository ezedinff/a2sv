'''
Lealem has given you a math expression that adds up a sequence of numbers and gave you a task.
Your task is to rearrange the numbers being added (not to add them) and
display the expression in a manner where the numbers are arranged in non-decreasing order.

Input
The first line contains the expression - s. s is not empty and contains no spaces.
It only contains digits "(1, 2, and 3)" and character "(+)". Besides, expression 𝑠
 is a correct sum. Expression 𝑠
 is at most 100 characters long.

Output
Print the new expression.

Examples
inputCopy
3+2+1
outputCopy
1+2+3
inputCopy
1+1+3+1+3
outputCopy
1+1+1+3+3
inputCopy
2
outputCopy
2

'''

def main():
    nums = map(int, input().split('+'))
    nums = sorted(nums)
    if len(nums) == 1:
        print(nums[0])
    else:
        print('+'.join(map(str, nums)))
