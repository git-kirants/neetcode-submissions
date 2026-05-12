class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if target in matrix[mid]:
                return True
            elif target > matrix[mid][0]:
                low = mid + 1
            else:
                high = mid - 1
        return False