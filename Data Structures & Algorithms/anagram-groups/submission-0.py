class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for ele in strs:
            count = [0] * 26
            for ch in ele:
                count[ord(ch) - ord('a')] += 1
            
            result[tuple(count)].append(ele)

        return list(result.values())
