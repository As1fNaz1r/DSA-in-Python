from typing import List
class Solution:
    def removeOuter(self, s:str)->int:
        openCount = 0
        res = ''
        for ch in s:
            if ch == '(':
                if openCount > 0:
                    res += ch
                openCount += 1
            else:
                openCount -= 1
                if openCount > 0:
                    res += ch

        return res

        
s = "(()())(())(()(()))"
solution = Solution()
print(solution.removeOuter(s))