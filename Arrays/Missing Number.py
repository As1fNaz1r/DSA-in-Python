from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in nums:
            total += i
        return n*(n+1)//2 - total


nums = [4, 5, 0, 1, 2, 3]

solution = Solution()
print(solution.missingNumber(nums))