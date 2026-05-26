class DynamicArray:
    
    def __init__(self, capacity: int):
        self.length = 0
        self.capacity = capacity
        self.arr = [0] * capacity


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.arr[self.length] = n
        self.length += 1


    def popback(self) -> int:
        if self.length == 0:
            return -1
        self.length -= 1 # think of indexes and how length is always the actual max index size + 1
        x = self.arr[self.length]
        self.arr[self.length] = 0
        return x


    def resize(self) -> None:
        self.capacity *= 2
        newArr = [0] * self.capacity

        for i, x in enumerate(self.arr):
            newArr[i] = x

        self.arr = newArr


    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
