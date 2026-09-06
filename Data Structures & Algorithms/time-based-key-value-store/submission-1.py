class TimeMap:

    def __init__(self):
        self.store = {} #will contain key + tuple of value and timestamp

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(value,timestamp)]
        else:
            self.store[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store: 
            return ""

        l = 0
        r = len(self.store[key]) - 1
        res = ""

        while l <= r:
            mid = (l+r) // 2
            v,t = self.store[key][mid]
            if t == timestamp:
                return v
            elif t < timestamp:
                res = v
                l = mid + 1
            else:
                r = mid - 1 

        return res


