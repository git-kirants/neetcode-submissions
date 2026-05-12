class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = Counter(nums)
        k= heapq.nlargest(1, count, key= lambda x: count[x])
        return k[0]