from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l=len(nums)
        for i in range(l):
            for j in range(i+1,l):
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
        print(nums)


solution = Solution()
solution.sortColors([2,0,2,1,1,0])