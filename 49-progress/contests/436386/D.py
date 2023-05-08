'''
You are given a rooted tree consisting of 𝑛
 vertices. Vertices are numbered from 1
 to 𝑛
. Any vertex can be the root of a tree.

A tree is a connected undirected graph without cycles. A rooted tree is a tree with a selected vertex, which is called the root.

The tree is specified by an array of parents 𝑝
 containing 𝑛
 numbers: 𝑝𝑖
 is a parent of the vertex with the index 𝑖
. The parent of a vertex 𝑢
 is a vertex that is the next vertex on the shortest path from 𝑢
 to the root. For example, on the simple path from 5
 to 3
 (the root), the next vertex would be 1
, so the parent of 5
 is 1
.

The root has no parent, so for it, the value of 𝑝𝑖
 is 𝑖
 (the root is the only vertex for which 𝑝𝑖=𝑖
).

Find such a set of paths that:

each vertex belongs to exactly one path, each path can contain one or more vertices;
in each path each next vertex — is a son of the current vertex (that is, paths always lead down — from parent to son);
number of paths is minimal.
For example, if 𝑛=5
 and 𝑝=[3,1,3,3,1]
, then the tree can be divided into three paths:

3→1→5
 (path of 3
 vertices),
4
 (path of 1
 vertices).
2
 (path of 1
 vertices).
Example of splitting a root tree into three paths for 𝑛=5
, the root of the tree — node 3
.
Input
The first line of input data contains an integer 𝑡
 (1≤𝑡≤104
) — the number of test cases in the test.

Each test case consists of two lines.

The first of them contains an integer 𝑛
 (1≤𝑛≤2⋅105
). It is the number of vertices in the tree.

The second line contains 𝑛
 integers 𝑝1,𝑝2,…,𝑝𝑛
 (1≤𝑝𝑖≤𝑛
). It is guaranteed that the 𝑝
 array encodes some rooted tree.

It is guaranteed that the sum of the values 𝑛
 over all test cases in the test does not exceed 2⋅105
.

Output
For each test case on the first line, output an integer 𝑚
 — the minimum number of non-intersecting leading down paths that can cover all vertices of the tree.

Then print 𝑚
 pairs of lines containing path descriptions. In the first of them print the length of the path, in the second — the sequence of vertices specifying that path in the order from top to bottom. You can output the paths in any order.

If there are several answers, output any of them.

Example
inputCopy
6
5
3 1 3 3 1
4
1 1 4 1
7
1 1 2 3 4 5 6
1
1
6
4 4 4 4 1 2
4
2 2 2 2
outputCopy
3
3
3 1 5
1
2
1
4

2
2
1 2
2
4 3

1
7
1 2 3 4 5 6 7

1
1
1

3
3
4 1 5
2
2 6
1
3

3
2
2 1
1
3
1
4

'''

def main():
    test_cases = int(input())
    for _ in range(test_cases): 
        n = int(input())
        parents = list(map(int, input().split()))
        find_paths(n, parents)

def find_paths(n, parents):
    children = [[] for _ in range(n)]
    for i, p in enumerate(parents):
        children[p - 1].append(i + 1)
    paths = []
    for i, c in enumerate(children):
        if c:
            paths.append([i + 1] + c)
    print(len(paths))
    for path in paths:
        print(len(path))
        print(*path)