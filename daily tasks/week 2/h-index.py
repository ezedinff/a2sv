# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return compute the researcher's h-index.
# According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."
# if there are several possible values for h, the maximum value of h is used.
# Example 1:
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3

# test cases
# citations = [1,3,1]
# output = 1

from typing import List
import unittest


def hIndex(citations: List[int]) -> int:
    # ct[i] = number papers with i-citations, this array will be later
    # modified to represent number of papers with at-least i-citations
    ct = [0] * (1 + max(citations))
    for c in citations:
        ct[c] += 1

    for h_idx in reversed(range(1, len(ct))):
        if ct[h_idx] >= h_idx:
            return h_idx

        # number of papers with at least h_idx - citations =
        # (number of papers with h_idx - 1) + (number of papers with more than h_idx - 1)
        ct[h_idx - 1] += ct[h_idx]

    return 0


class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(hIndex([3, 0, 6, 1, 5]), 3)

    def test_2(self):
        self.assertEqual(hIndex([1, 3, 1]), 1)