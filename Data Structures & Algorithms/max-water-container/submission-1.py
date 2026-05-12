class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0  
        r = len(heights) - 1
        volume = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            volume = max(volume, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return volume