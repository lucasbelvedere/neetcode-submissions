class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        cleaner = ''.join(c for c in s if c.isalnum()).lower()
        right = len(cleaner) - 1

        while left < right:
            if cleaner[left] != cleaner[right]:
                return False
            left += 1
            right -= 1

        return True