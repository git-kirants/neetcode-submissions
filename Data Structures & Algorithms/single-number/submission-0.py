class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = [key for key, value in count.items() if value == 1]
        return ans[0]