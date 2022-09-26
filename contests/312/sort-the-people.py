# Sort the people
'''
You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.

Example 1:

Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.

'''

class Solution:
    def sortPeople(self, names, heights):
        
        # create a dictionary of heights and names
        height_dict = {}
        for i in range(len(names)):
            height_dict[heights[i]] = names[i]
        
        # sort the heights
        heights.sort(reverse=True)
        
        # create a new list of names
        names = []
        for height in heights:
            names.append(height_dict[height])
        
        return names

# Test
names = ["Mary","John","Emma"]
heights = [180,165,170]
s = Solution()
print(s.sortPeople(names, heights))