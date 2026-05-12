class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        
        for i in range(len(nums)):
            req = target - nums[i]
            if req in d:
                return [d[req], i]
            d[nums[i]] = i
