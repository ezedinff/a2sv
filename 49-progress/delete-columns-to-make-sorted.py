# 944. Delete Columns to Make Sorted
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for i in range(len(strs[0])): # columns
            for j in range(len(strs) - 1): # rows
                if ord(strs[j][i]) > ord(strs[j+1][i]): # check if the character is greater than the one below it
                    count += 1
                    break # break and continue to the next column
        return count

# e