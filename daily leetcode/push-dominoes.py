# push dominoes
# leetcode https://leetcode-cn.com/problems/push-dominoes/

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = "L" + dominoes + "R"
        res = ""
        i = 0
        for j in range(1, len(dominoes)):
            if dominoes[j] == ".":
                continue
            middle = j - i - 1
            if i:
                res += dominoes[i]
            if dominoes[i] == dominoes[j]:
                res += dominoes[i] * middle
            elif dominoes[i] == "L" and dominoes[j] == "R":
                res += "." * middle
            else:
                res += "R" * (middle // 2) + "." * (middle % 2) + "L" * (middle // 2)
            i = j
        return res

if __name__ == "__main__":
    dominoes = "RR.L"
    assert Solution().pushDominoes(dominoes) == "RR.L"
    dominoes = ".L.R...LR..L.."
    assert Solution().pushDominoes(dominoes) == "LL.RR.LLRRLL.."