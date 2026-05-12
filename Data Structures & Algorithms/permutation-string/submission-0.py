from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1 = Counter(s1)
        count2 = Counter(s2[:len(s1)])
        if count1 == count2:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            count2[s2[r]] += 1
            left_char = s2[l]
            count2[left_char] -= 1
            if count2[left_char] == 0:
                del count2[left_char]
            l += 1
            if count1 == count2:
                return True
        return False