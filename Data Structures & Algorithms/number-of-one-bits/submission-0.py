class Solution:
    def hammingWeight(self, n: int) -> int:
        count = Counter(bin(n))
        return count["1"]