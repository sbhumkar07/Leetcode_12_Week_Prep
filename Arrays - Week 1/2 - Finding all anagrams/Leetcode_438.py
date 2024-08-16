class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        sCounter, pCounter = {}, {}
        for x in range(len(p)):
            sCounter[s[x]] = 1 + sCounter.get(s[x], 0)
            pCounter[p[x]] = 1 + pCounter.get(p[x], 0)
        
        result = [0] if sCounter == pCounter else []
        
        leftPtr = 0
        for rightPtr in range(len(p), len(s)):
            sCounter[s[rightPtr]] = 1 + sCounter.get(s[rightPtr], 0)
            sCounter[s[leftPtr]] -= 1
            
            if sCounter[s[leftPtr]] == 0:
                sCounter.pop(s[leftPtr])
            
            leftPtr += 1
            if sCounter == pCounter:
                result.append(leftPtr)

        return result
