class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}

        for ele in s:
            count[ele] = count.get(ele, 0) + 1

        for ele in t:
            count[ele] = count.get(ele, 0) - 1
            if  count[ele] == 0:
                del count[ele]

        return not count