class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res, left, prev = 1, 0, ""
        for right in range(1, len(arr)):
            if arr[right - 1] > arr[right] and prev != ">":
                res = max(res, right - left + 1)
                prev = ">"
            elif arr[right - 1] < arr[right] and prev != "<":
                res = max(res, right - left + 1)
                prev = "<"
            else:
                if arr[right] != arr[right - 1]:
                    left = right - 1
                    prev = ">" if arr[right - 1] > arr[right] else "<"
                else:
                    left = right
                    prev = ""
        return res