# minimum number of jumps
# Given an array of integers where each element represents the max number of steps that can be made forward from that element.

# Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
# Output: 3 (1-> 3 -> 8 ->9)


class Solution:
    def minJumps(self, arr, n):
        # code here
        if n == 1:
            return 0
        if arr[0] == 0:
            return -1
        max_reach = arr[0]
        steps = arr[0]
        jumps = 1
        for i in range(1, n):
            if i == n - 1:
                return jumps
            max_reach = max(max_reach, i + arr[i])
            steps -= 1
            if steps == 0:
                jumps += 1
                if i >= max_reach:
                    return -1
                steps = max_reach - i
        return -1