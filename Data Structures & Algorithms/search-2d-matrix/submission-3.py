class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[-1])
        left, right = 0, (n * m) - 1 # m x n
        while left <= right:
            mid = (left + right) // 2
            row = mid // m
            col = mid % m
            if matrix[row][col] > target:
                right = mid - 1
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                return True
        return False