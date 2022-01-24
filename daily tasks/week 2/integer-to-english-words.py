# integer to english words
# convert a non-negative integer num to its English words representation.
# Example 1:
# Input: num = 123
# Output: "One Hundred Twenty Three"

from collections import deque
import unittest


def numberToWords(num: int) -> str:
    # 1-9
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    # 10-19
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    # 20-90
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    # 100-900
    hundreds = ["", "One Hundred", "Two Hundred", "Three Hundred", "Four Hundred", "Five Hundred", "Six Hundred", "Seven Hundred", "Eight Hundred", "Nine Hundred"]
    # 1000-9000
    thousands = ["", "Thousand", "Million", "Billion"]
    
    queue = deque()
    if num == 0:
        return "Zero"

    while num > 0:
        queue.appendleft(num % 1000)
        num //= 1000
    res = ""
    while len(queue) > 0:
        num = queue.popleft()
        if num == 0:
            continue
        if num >= 100:
            res += hundreds[num // 100] + " "
            num %= 100
        if num >= 20:
            res += tens[num // 10] + " "
            num %= 10
        if num >= 10:
            res += teens[num - 10] + " "
        if num >= 1:
            res += ones[num] + " " if num <= len(ones) - 1 else ""
        if len(queue) > 0:
            res += thousands[len(queue)] + " "
    return res.strip()


class TestSolution(unittest.TestCase):
    # test case 1
    def test_case_1(self):
        self.assertEqual(numberToWords(123), "One Hundred Twenty Three")
    
    # test case 2
    def test_case_2(self):
        self.assertEqual(numberToWords(0), "Zero")
    
    # test case 3
    def test_case_3(self):
        self.assertEqual(numberToWords(1234567891), "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One")



if __name__ == '__main__':
    unittest.main()