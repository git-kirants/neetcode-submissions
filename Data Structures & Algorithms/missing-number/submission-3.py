class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i, a in enumerate(nums):
            if i != a:
                return i
        return len(nums)