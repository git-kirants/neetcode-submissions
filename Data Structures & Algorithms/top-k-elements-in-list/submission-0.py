class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for ele in nums:
            count[ele] = count.get(ele, 0) + 1
        
        return heapq.nlargest(k, count, key=lambda x: count[x])