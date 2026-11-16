'''
Input: a string s
Output: a list of lists of strings, with every possible way to split s so that each substring is a palindrome

Approach: backtracking with a decision tree, like the following illustration:

                         start (i=0, [])
            /                  |                   \
        "a" ✓                "aa" ✓              "aab" ✗ (PRUNE)
     i=1, ["a"]            i=2, ["aa"]
       /       \                |
   "a" ✓      "ab" ✗          "b" ✓
 i=2, ["a","a"]  (PRUNE)   i=3, ["aa","b"]  (ADD)
      |
    "b" ✓
 i=3, ["a","a","b"] (ADD)

The decision tree works like this: starting at index i, we grow a substring one character at a time. Whenever the substring is a palindrome, we add it to temp and recursively call the helper function on the rest of the string to see if it can also be split into palindromes. Once the call returns, we pop the substring from temp and keep extending it with the next character, checking again if it's a palindrome. If it is, we add it to temp and call recursively again. When i reaches the end of the string, temp holds a valid split, so we add a copy of it to res.

PLAN:
- res, temp = [], []
- declare and initialize backtrack that takes i:
    - if i == len(s):
        - res.append(temp.copy())
        - return

    - s_copy = ""
    - for j in range(i, len(s)):
        - s_copy += s[j]
        - if isPalindrome(s_copy):
            - temp.append(s_copy)
            - backtrack(j + 1)
            - temp.pop()
- backtrack(0)
- return res

- declare a function called isPalindrome that takes s:
    - left, right = 0, len(s) - 1
    - while left < right:
        - if s[left] != s[right]:
            - return False
        - left += 1
        - right -= 1
    - return True

Time complexity: O(n * 2^n). The 2^n comes from the number of ways to split the string (each gap between characters is either a cut or not), and the n comes from isPalindrome and from copying temp into res.
Space complexity: O(n) for the height of the recursion stack and temp, not counting the output.
'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, temp = [], []

        def backtrack(i):
            if i == len(s):
                res.append(temp.copy())
                return
            
            s_copy = ""
            for j in range(i, len(s)):
                s_copy += s[j]
                if self.isPalindrome(s_copy):
                    temp.append(s_copy)
                    backtrack(j + 1)
                    temp.pop()

        backtrack(0)
        return res     

    def isPalindrome(self, s):
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
        