# number of good paths
'''
There is a tree (i.e. a connected, undirected graph with no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges.

You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node. You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

A good path is a simple path that satisfies the following conditions:

The starting node and the ending node have the same value.
All nodes between the starting node and the ending node have values less than or equal to the starting node (i.e. the starting node's value should be the maximum value along the path).
Return the number of distinct good paths.

Note that a path and its reverse are counted as the same path. For example, 0 -> 1 is considered to be the same as 1 -> 0. A single node is also considered as a valid path.

Example 1:
Input: vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]
Output: 6
Explanation: There are 5 good paths consisting of a single node.
There is 1 additional good path: 1 -> 0 -> 2 -> 4.
(The reverse path 4 -> 2 -> 0 -> 1 is treated as the same as 1 -> 0 -> 2 -> 4.)
Note that 0 -> 2 -> 3 is not a good path because vals[2] > vals[0].
'''

from collections import defaultdict
from typing import List

class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n
        self.freq = [defaultdict(int) for _ in range(n)]

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b, v):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]
            
            q = self.freq[a][v] * self.freq[b][v]
            
            for k in self.freq[b]:
                self.freq[a][k] += self.freq[b][k]
            return q
        return 0

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        dsu = DisjointSetUnion(n)
        
        for i in range(n):
            dsu.freq[i][vals[i]] = 1
        
        g = defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            
        s = defaultdict(list)
        for i, v in enumerate(vals):
            s[v].append(i)
            
        seen = set()
        ret = 0
        for k in sorted(list(s.keys())):
            for x in s[k]:
                seen.add(x)
                for y in g[x]:
                    if y in seen:
                        ret += dsu.union(x, y, k)
                        # print(x, y, ret)
        return ret + n
                        
if __name__ == '__main__':
    solution = Solution()
    assert solution.numberOfGoodPaths([1,3,2,1,3], [[0,1],[0,2],[2,3],[2,4]]) == 6
