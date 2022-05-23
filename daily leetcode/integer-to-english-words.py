"""

Input: num = 123
Output: "One Hundred Twenty Three"

"""


class Solution:
    less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                    "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        ans = ""
        i = 0
        while num > 0:
            if num % 1000 != 0:
                ans = self.helper(num % 1000) + Solution.thousands[i] + " " + ans
            i += 1
            num //= 1000
        return ans.strip()

    def helper(self, n):
        if n == 0:
            return ""
        elif n < 20:
            return Solution.less_than_20[n] + " "
        elif n < 100:
            return Solution.tens[n // 10] + " " + self.helper(n % 10)
        else:
            return Solution.less_than_20[n // 100] + " Hundred " + self.helper(n % 100)


s = Solution()
assert s.numberToWords(123) == "One Hundred Twenty Three"
