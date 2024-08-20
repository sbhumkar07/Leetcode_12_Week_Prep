class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        substringSet = set()
        for right in range(len(s)):
            while s[right] in substringSet:
                substringSet.remove(s[left])
                left += 1
            
            substringSet.add(s[right])
            longest = max(longest, right - left +1)
        return longest
