'''
A company has 𝑛
 employees numbered from 1
 to 𝑛
. Each employee either has no immediate manager or exactly one immediate manager, who is another employee with a different number. An employee 𝐴
 is said to be the superior of another employee 𝐵
 if at least one of the following is true:

Employee 𝐴
 is the immediate manager of employee 𝐵
Employee 𝐵
 has an immediate manager employee 𝐶
 such that employee 𝐴
 is the superior of employee 𝐶
.
The company will not have a managerial cycle. That is, there will not exist an employee who is the superior of his/her own immediate manager.

Today the company is going to arrange a party. This involves dividing all 𝑛
 employees into several groups: every employee must belong to exactly one group. Furthermore, within any single group, there must not be two employees 𝐴
 and 𝐵
 such that 𝐴
 is the superior of 𝐵
.

What is the minimum number of groups that must be formed?

Input
The first line contains integer 𝑛
 (1≤𝑛≤2000
) — the number of employees.

The next 𝑛
 lines contain the integers 𝑝𝑖
 (1≤𝑝𝑖≤𝑛
 or 𝑝𝑖=
-1). Every 𝑝𝑖
 denotes the immediate manager for the 𝑖
-th employee. If 𝑝𝑖
 is -1, that means that the 𝑖
-th employee does not have an immediate manager.

It is guaranteed, that no employee will be the immediate manager of him/herself (𝑝𝑖≠𝑖
). Also, there will be no managerial cycles.

* don't forgot that its 1-indexed

Output
Print a single integer denoting the minimum number of groups that will be formed in the party.

Examples
inputCopy
5
-1
1
2
1
-1
outputCopy
3
Note
For the first example, three groups are sufficient, for example:

Employee 1
Employees 2 and 4
Employees 3 and 5
'''

def main():
    n = int(input())
    max_depth = 0    
    managers = [0] + [int(input()) for _ in range(n)]
 
    for i in range(1, n + 1):
        depth = 0
        while managers[i] != -1:
            i = managers[i]
            depth += 1
        max_depth = max(max_depth, depth)
    print(max_depth + 1)

main()