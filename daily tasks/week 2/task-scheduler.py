"""
https://leetcode.com/problems/task-scheduler/
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different
task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could
complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same
letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.



Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation:
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.


Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation:
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
"""
import unittest
from typing import List


def leastInterval(tasks: List[str], n: int) -> int:
    frequencies = [0 for i in range(26)]
    for task in tasks:
        frequencies[ord(task) - ord('A')] += 1
    frequencies.sort()
    max_val = frequencies[-1] - 1
    idle_slots = max_val * n

    for i in range(24, -1, -1):
        idle_slots -= min(max_val, frequencies[i])

    return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)


class TestSolution(unittest.TestCase):
    def test_1(self):
        tasks, n = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2
        expected = 16
        actual = leastInterval(tasks, n)
        self.assertEqual(expected, actual)

    def test_1(self):
        tasks, n = ["A", "A", "A", "B", "B", "B"], 2
        expected = 8
        actual = leastInterval(tasks, n)
        self.assertEqual(expected, actual)

    def test_3(self):
        tasks, n = ["A", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                    "T", "U", "V", "W", "X", "Y", "Z"], 29
        expected = 31
        actual = leastInterval(tasks, n)
        self.assertEqual(expected, actual)
