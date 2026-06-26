class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left, maxSize = 0, 0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            maxSize = max(maxSize, len(charSet))
        return maxSize