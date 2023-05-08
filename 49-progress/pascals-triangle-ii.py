# 119. Pascal's Triangle II
from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def helper(rowIndex):
            if rowIndex == 0:
                return [1]
            if rowIndex == 1:
                return [1,1]
            res = [1]
            pre = helper(rowIndex-1)
            for i in range(len(pre)-1):
                res.append(pre[i]+pre[i+1])
            res.append(1)
            return res
        return helper(rowIndex)