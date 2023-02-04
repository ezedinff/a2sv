# 1122. Relative Sort Array
'''
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

 

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
Example 2:

Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]
'''

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = {}
        for i in range(len(arr2)):
            ans[arr2[i]] = i
        arr1.sort(key = lambda x: ans[x] if x in ans else x + 1000)
        return arr1
# explaination:
# we use a dictionary to store the index of each element in arr2
# then we sort arr1 by the index of each element in arr2
# if the element is not in arr2, we add 1000 to it so that it will be at the end of the sorted array
# Time: O(nlogn)

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort(key = lambda x: (0, arr2.index(x)) if x in arr2 else (1, x))
        return arr1
