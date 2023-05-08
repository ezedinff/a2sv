from typing import List

class Solution:
  def sumSubarrayMins(self, arr: List[int]) -> int:
    kMod = 1_000_000_007
    n = len(arr)
    ans = 0
    # prev[i] := index k s.t. arr[k] is the prev min in arr[:i]
    prev = [-1] * n
    # next[i] := index k s.t. arr[k] is the next min in arr[i + 1:]
    next = [n] * n
    stack = []

    for i, a in enumerate(arr):
      while stack and arr[stack[-1]] > a:
        index = stack.pop()
        next[index] = i
      if stack:
        prev[i] = stack[-1]
      stack.append(i)

    for i, a in enumerate(arr):
      ans += a * (i - prev[i]) * (next[i] - i)
      ans %= kMod

    return ans

'''
Explanation of the solution

Let's consider the subarray arr[i:j] where i < j.
We can split this subarray into two parts: arr[i:k] and
arr[k:j] where i < k < j. The minimum value in arr[i:j]
is the minimum of arr[i:k] and arr[k:j].
We can use this observation to solve the problem.


'''


class Solution:
  def sumSubarrayMins(self, arr: List[int]) -> int:
    ans = 0
    stack = []
    for i, a in enumerate(arr):
        while stack and stack[-1][0] > a:
            stack.pop()
        if stack:
            ans += a * (i - stack[-1][1]) * (stack[-1][1] - stack[-1][0])
        stack.append((i, a))
    return ans
