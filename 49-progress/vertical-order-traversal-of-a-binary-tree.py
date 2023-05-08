from collections import deque
from typing import List, Optional
from data_structures import TreeNode

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = {}  # hash table to store nodes at each horizontal distance
        queue = deque([(root, 0, 0)])  # level-order traversal queue
        while queue:
            node, hd, vd = queue.popleft()
            if node:
                if hd not in d:
                    d[hd] = []
                d[hd].append((vd, node.val))
                queue.append((node.left, hd - 1, vd + 1))
                queue.append((node.right, hd + 1, vd + 1))
        res = []
        for hd in sorted(d.keys()):
            nodes = d[hd]
            nodes.sort(key=lambda x: (x[0], x[1]))  # sort by vd and then by val
            res.append([node[1] for node in nodes])
        return res