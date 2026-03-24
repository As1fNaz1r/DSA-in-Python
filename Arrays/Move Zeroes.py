from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0 
        for j in nums:
            if j !=0:
                nums[i] = j
                i += 1
        while i < len(nums):
            nums[i] = 0
            i += 1

nums = [0, 1, 0, 0, 2, 3]
solution = Solution()
solution.moveZeroes(nums)
print(nums)