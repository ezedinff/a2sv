'''
Greg has an array a = a1, a2, ..., an and m operations. Each operation looks as: li, ri, di, (1 ≤ li ≤ ri ≤ n). To apply operation i to the array means to increase all array elements with numbers li, li + 1, ..., ri by value di.

Greg wrote down k queries on a piece of paper. Each query has the following form: xi, yi, (1 ≤ xi ≤ yi ≤ m). That means that one should apply operations with numbers xi, xi + 1, ..., yi to the array.

Now Greg is wondering, what the array a will be after all the queries are executed. Help Greg.

Input
The first line contains integers n, m, k (1 ≤ n, m, k ≤ 105). The second line contains n integers: a1, a2, ..., an (0 ≤ ai ≤ 105) — the initial array.

Next m lines contain operations, the operation number i is written as three integers: li, ri, di, (1 ≤ li ≤ ri ≤ n), (0 ≤ di ≤ 105).

Next k lines contain the queries, the query number i is written as two integers: xi, yi, (1 ≤ xi ≤ yi ≤ m).

The numbers in the lines are separated by single spaces.

Output
On a single line print n integers a1, a2, ..., an — the array after executing all the queries. Separate the printed numbers by spaces.

Please, do not use the %lld specifier to read or write 64-bit integers in C++. It is preferred to use the cin, cout streams of the %I64d specifier.

Examples
inputCopy
3 3 3
1 2 3
1 2 1
1 3 2
2 3 4
1 2
1 3
2 3
outputCopy
9 18 17
inputCopy
1 1 1
1
1 1 1
1 1
outputCopy
2
inputCopy
4 3 6
1 2 3 4
1 2 1
2 3 2
3 4 4
1 2
1 3
2 3
1 2
1 3
2 3
outputCopy
5 18 31 20
'''


def main():
    n, m, k = map(int, input().split())
    array = list(map(int, input().split()))
    operations = []
    for i in range(m):
        operation = list(map(int, input().split()))
        operations.append(operation)
    queries = []
    for i in range(k):
        query = list(map(int, input().split()))
        queries.append(query)
    operations_ = [0] * (m + 1)
    array_ = [0] * (n + 1)
    acumulado = 0
    acumulado_ = 0
    for i in queries:
        operations_[i[0] - 1] += 1
        operations_[i[1]] -= 1
    for i in range(m):
        acumulado_ += operations_[i]
        array_[operations[i][0] - 1] += operations[i][2] * acumulado_
        array_[operations[i][1]] -= operations[i][2] * acumulado_
    for i in range(n):
        acumulado += array_[i] 
        array[i] += acumulado
    print(' '.join(map(str, array)))


'''
The problem statement describes an array a of length n and m operations that can be applied to the array.
Each operation i is described by three integers: li, ri, and di,
indicating that all elements in the array between li and ri inclusive should be increased by di.
In addition, there are k queries, each query consisting of two integers xi and yi.
The task is to apply all operations in the range xi to yi inclusive and then output
the final state of the array.

The given solution first reads in the input values n, m, and k, as well as the initial array a.
It then reads in the m operations and k queries and stores them in operations and queries lists respectively.

The solution then creates two new arrays, operations_ and array_, both of which are initialized to 0.
operations_ has a length of m+1, and array_ has a length of n+1. The purpose of operations_ is
to keep track of how many queries each operation is included in, and the purpose of array_ is
to store the changes that are made to the array as a result of the operations.

The solution then iterates over the queries list and increments the corresponding values in operations_.
The operations_ list is then used to calculate the cumulative effect of the operations in array_.
Specifically, the solution iterates over each operation and multiplies its value by the corresponding
value in operations_. The result is then stored in array_, with array_[li-1] being
incremented by di * operations_[i] and array_[ri] being decremented by di * operations_[i].

Finally, the solution iterates over array_ and accumulates the values, storing the result in acumulado.
It then updates the values of array by adding acumulado to each element. Finally, the solution prints
the final state of the array.

Overall, this solution uses an efficient approach to solve the problem by calculating the cumulative
effect of the operations and applying them to the array in a single pass.
'''