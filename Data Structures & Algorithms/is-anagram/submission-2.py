class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the strings are anagrams, that means total count of characters in both strings MUST be an even number
        count_char1, count_char2 = {}, {}
        
        for char in s:
            if char not in count_char1:
                count_char1[char] = 1
            else:
                count_char1[char] += 1

        for char in t:
            if char not in count_char2:
                count_char2[char] = 1
            else:
                count_char2[char] += 1

        for k, v in count_char1.items():
            if k not in count_char2:
                return False
            elif count_char1[k] != count_char2[k]:
                return False

        for k, v in count_char2.items():
            if k not in count_char1:
                return False
        
        return True
