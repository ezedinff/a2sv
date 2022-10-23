# Dam of candies

# Geek wants to make a special space for candies on his bookshelf. 
# Currently, it has N books, each of whose height is represented by the array height[] and has unit width.
# Help him select 2 books such that he can store the maximum candies
# between them by removing the other books from between the selected books. The task is to find out the area between 2 books that can hold the maximum candies without changing the original position of selected books.

# Example 1:
# Input: N = 3, height[] = {1, 3, 4}
# Output: 1

class Solution:
    def maxCandy(self, height, n):
        # code here
        i, j, max_area = 0, n - 1, 0
        while i < j:
            max_area = max(max_area, (j - i - 1) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area