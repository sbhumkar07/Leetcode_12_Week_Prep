class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest,left = 0, 0
        sCount = [0] * 26
        
        for right in range(len(s)):
            sCount[ord(s[right])-ord('A')] += 1
            while (right - left + 1) - max(sCount) > k:
                sCount[ord(s[left])-ord('A')] -= 1
                left +=1
            longest = max(longest, (right - left + 1))
        return longest
            
