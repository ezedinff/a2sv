class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                j = stack.pop()
                result[j] = i - j
            stack.append(i)
        return result
    # technique is to use a stack to keep track of the indices of the temperatures
    # if the current temperature is greater than the temperature at the top of the stack
    # then we know that the current temperature is the first day that is warmer than the
    # temperature at the top of the stack
    # we can then pop the top of the stack and calculate the difference between the current
    # index and the index of the temperature at the top of the stack
    # we can then store the difference in the result array at the index of the temperature
    # at the top of the stack
    # we can then push the current index onto the stack
    # we can then repeat this process until the stack is empty or the current temperature
    # is less than or equal to the temperature at the top of the stack