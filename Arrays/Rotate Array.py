from typing import List
class Solution:
    def rotate(self, nums: List[int], k : int) -> List[int]:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums


nums = [1, 2, 3, 4, 5, 6, 7]
solution = Solution()
print(solution.rotate(nums, 3))