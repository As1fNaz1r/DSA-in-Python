from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currentOnes = 0
        maxOnes = 0
        for i in nums:
            if i==1:
                currentOnes = currentOnes + 1
            else:
                currentOnes = 0
                maxOnes = max(maxOnes, currentOnes)
        return max(maxOnes, currentOnes)
nums = [1,1,0,1,1,1]
solution = Solution()
print(solution.findMaxConsecutiveOnes(nums))