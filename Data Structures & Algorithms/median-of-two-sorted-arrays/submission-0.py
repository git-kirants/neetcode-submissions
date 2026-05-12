class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = sorted(nums1 + nums2)
        length = len(n)
        mid = length // 2

        if length % 2:
            return n[mid]
        else:
            return (n[mid - 1] + n[mid]) / 2