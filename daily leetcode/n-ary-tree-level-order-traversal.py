class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            new_queue = []
            res.append([node.val for node in queue])
            for node in queue:
                new_queue.extend(node.children)
            queue = new_queue
        return res