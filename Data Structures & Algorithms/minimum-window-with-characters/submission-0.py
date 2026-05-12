class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if s == t:
            return s
        
        if len(s) < len(t):
            return ""

        
        countT = Counter(t)
        window = {}
        l = have = 0
        need = len(countT)
        res = [-1,-1]
        resL = float("infinity")


        for r, ch in enumerate(s):
            window[ch] = 1 +  window.get(ch, 0)
            if ch in countT and window[ch] == countT[ch]:
                have += 1
            
            while have == need:
                if (r-l+1) < resL:
                    res = [l,r]
                    resL = r-l+1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        return s[l:r+1] if resL != float("infinity") else ""