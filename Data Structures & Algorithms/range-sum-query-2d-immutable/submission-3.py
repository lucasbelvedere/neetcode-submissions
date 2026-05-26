class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [0] * len(matrix) * len(matrix[0]) # array with size n x m, where n is num of rows, and m is num of columns
        self.matrix = matrix
        for i in range(len(matrix)):
            sum = 0
            for j in range(len(matrix[i])):
                index = i * len(matrix[0]) + j              
                sum += matrix[i][j]
                self.prefix[index] = sum
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        cols = len(self.matrix[0])
        sumRegion = 0
        for i in range(row1, row2 + 1):
            index_1 = i * cols + col2
            sumRegion += self.prefix[index_1]
            if col1 > 0:
                index_2 = i * cols + (col1 - 1)
                sumRegion -= self.prefix[index_2]
        return sumRegion
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)