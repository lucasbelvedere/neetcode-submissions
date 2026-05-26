class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        newArr = [0] * (2 * n)

        for i, x in enumerate(nums):
            newArr[i] = x
            newArr[i + n] = x

        return newArr