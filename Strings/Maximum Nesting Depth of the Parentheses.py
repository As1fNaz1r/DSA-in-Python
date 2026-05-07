from typing import List

class Solution:
    def maxDepth(self, s:str)->int:
        n = len(s)
        i = 0
        currD = 0
        maxD = 0
        for i in range(n):
            if s[i]=='(':
                currD += 1
                maxD = max(currD, maxD)
            elif s[i]==')':
                currD -= 1
        return maxD

s = "(1+(2*3)+((8)/4))+1"
solution = Solution()
print((solution.maxDepth(s)))