class TimeMap:

    def __init__(self):
        self.store = {} # key = string, value = [list of [value, timestamp]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp]) # O(1)

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        # binary search
        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2

            if values[mid][1] <= timestamp: # less than or equal in this case, since if we don't have a time equal to the timestamp, we just return the closest to it
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res
        
