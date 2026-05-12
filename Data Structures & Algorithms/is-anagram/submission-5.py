class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:
            count[ch] = count.get(ch, 0) - 1
            if count[ch] == 0:
                del count[ch]
        
        return not count