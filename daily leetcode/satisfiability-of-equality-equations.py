# Satisfiability of Equality Equations
# https://leetcode.com/problems/satisfiability-of-equality-equations/

from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        parent = {chr(i): chr(i) for i in range(ord('a'), ord('z') + 1)}
        for e in equations:
            if e[1] == '=':
                union(e[0], e[3])
        for e in equations:
            if e[1] == '!' and find(e[0]) == find(e[3]):
                return False
        return True

if __name__ == '__main__':
    assert Solution().equationsPossible(["a==b","b!=a"]) == False
    assert Solution().equationsPossible(["b==a","a==b"]) == True
    assert Solution().equationsPossible(["a==b","b==c","a==c"]) == True
    assert Solution().equationsPossible(["a==b","b!=c","c==a"]) == False
    assert Solution().equationsPossible(["c==c","b==d","x!=z"]) == True