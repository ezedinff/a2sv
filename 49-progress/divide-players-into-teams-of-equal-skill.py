from typing import List
'''
You are given a positive integer array skill of even length n where skill[i]
denotes the skill of the ith player. Divide the players into n / 2 teams of
size 2 such that the total skill of each team is equal.

The chemistry of a team is equal to the product of the skills of the
 players on that team.

Return the sum of the chemistry of all the teams, or return -1 if there
is no way to divide the players into teams such that the total skill of
each team is equal.

Example 1:
Input: skill = [3,2,5,1,3,4]
Output: 22
Explanation: 
Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.

Input: skill = [1,1,2,3]
Output: -1
Explanation: 
There is no way to divide the players into teams such that the total skill of each team is equal.
'''

'''
The solution uses the two-pointer approach to divide the players into teams of equal total skill.

Here's how it works:

- Sort the array of skills in ascending order.
- Calculate the target skill value for each team by dividing the sum of all skills by the number of teams (n // 2).

- Check if the target skill value is obtainable by multiplying the number of teams by the target skill value.
 If it is not,
 return -1 as there is no way to divide the players into teams of equal total skill.

- Set two pointers, left and right, pointing to the beginning and end of the sorted array.

- While the left pointer is less than the right pointer, compare the sum of the skills of the players
 at the left and right pointers with the target skill value.
- If they are equal, increment the result by the product of their skills, move the left pointer
 to the right by one step, and move the right pointer to the left by one step.
- If they are less than the target skill value, move the left pointer to the right by one step.
- If they are greater than the target skill value, move the right pointer to the left by one step.
- Return the result.

This solution has a time complexity of O(n log n) due to sorting the array of skills,
and a space complexity of O(1) since we only use variables to store the result, target skill value,
and two pointers.

'''


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        target = sum(skill) // (n // 2)
        if target * (n // 2) != sum(skill):
            return -1
        left = 0
        right = n - 1
        result = 0
        while left < right:
            if skill[left] + skill[right] == target:
                result += skill[left] * skill[right]
                left += 1
                right -= 1
            elif skill[left] + skill[right] < target:
                left += 1
            else:
                right -= 1
        return result if result > 0 else -1
