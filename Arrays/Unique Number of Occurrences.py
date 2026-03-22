from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occ = {}
        for num in arr:
            if num in occ:
                occ[num] += 1
            else:
                occ[num] = 1
        return len(occ.values()) == len(set(occ.values()))

nums  = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

solution = Solution()
print(solution.uniqueOccurrences(nums))