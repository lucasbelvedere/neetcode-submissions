class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return list(strs)

        anagrams = defaultdict(list)
        for word in strs:
            freq_char = [0]*26 # count every char in the alphabet
            for char in word:
                freq_char[ord(char) - ord("a")] += 1 # ord returns the ascii code
            hashable_k = tuple(freq_char) # hashable key
            anagrams[hashable_k].append(word)

        return list(anagrams.values())