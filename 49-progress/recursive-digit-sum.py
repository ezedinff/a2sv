#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    if len(n) == 1:
        return int(n)
    else:
        res = 0
        for i in n:
            res += int(i)
        res *= k
        return superDigit(str(res),1)