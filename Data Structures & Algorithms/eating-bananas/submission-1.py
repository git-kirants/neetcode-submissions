class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        
        piles.sort()
        low = 1
        high = max(piles)
        res = []
        while low < high:
            mid = low + (high - low) // 2
            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid
            if hours > h:
                low = mid + 1
            else:
                high = mid

        return low
