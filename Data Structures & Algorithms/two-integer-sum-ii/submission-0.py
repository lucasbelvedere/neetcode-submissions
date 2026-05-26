class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        twoSum = numbers[left] + numbers[right]
        while twoSum != target and left < right:
            if twoSum < target:
                left += 1
            else:
                right -= 1
            print("left: ", left, " ... right: ", right)
            twoSum = numbers[left] + numbers[right]

        return [left + 1, right + 1]