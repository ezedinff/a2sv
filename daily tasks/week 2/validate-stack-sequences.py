import unittest
from typing import List


def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    storage = []
    pop_count = 0
    for item in pushed:
        storage.append(item)
        while storage and pop_count < len(popped) and storage[-1] == popped[pop_count]:
            storage.pop()
            pop_count += 1

    return pop_count == len(popped)


# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]

class TestSolutions(unittest.TestCase):
    def test_one(self):
        pushed, popped = [1, 2, 3, 4, 5], [4, 5, 3, 2, 1]
        actual = validateStackSequences(pushed, popped)
        expected = True
        self.assertEqual(expected, actual)

    def test_two(self):
        pushed, popped = [1, 2, 3, 4, 5], [4, 3, 5, 1, 2]
        actual = validateStackSequences(pushed, popped)
        expected = False
        self.assertEqual(expected, actual)
