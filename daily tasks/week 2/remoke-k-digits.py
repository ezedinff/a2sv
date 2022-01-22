# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

# 1.interate over the string from left to right
# 2.create deque which saves the digits to be returned
# 3.push char of the string into the deque
# 4.if current char is lessthan back of deque and k>0 pop and push the char
# 5.then decrease k by 1
# 6.after the iteration ends if k is greater than 0 pop k elements from the deque
# 7.zero is an edge case here if the deque contains only zero and if there exist leading zero
import collections
import unittest


def removeKdigits(num: str, k: int) -> str:
    deque = collections.deque()
    for i in range(len(num)):
        while k > 0 and deque and deque[-1] > num[i]:
            deque.pop()
            k -= 1
        deque.append(num[i])
    while deque and k:
        deque.pop()
        k -= 1

    count = collections.Counter(deque)
    if count["0"] == len(deque):
        return "0"

    while deque and deque[0] == '0':
        deque.popleft()

    return ''.join(deque)


class TestSolution(unittest.TestCase):
    def test_1(self):
        num, k = "1432219", 3
        expected = "1219"
        actual = removeKdigits(num, k)
        self.assertEqual(expected, actual)
