class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ''.join(c for c in s if c.isalnum()).lower()
        left, right = 0, len(palindrome) - 1

        while left <= right:
            if palindrome[left] != palindrome[right]:
                return False
            left += 1
            right -= 1

        return True