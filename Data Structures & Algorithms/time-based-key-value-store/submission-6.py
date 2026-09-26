class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((value,timestamp))
        else:
            self.store[key] = [(value,timestamp)]

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.store:
            return ""
        
        if key in self.store:
            if timestamp < self.store[key][0][1]:
                return ""

        if key in self.store: 
            l, r = 0, len(self.store[key])-1
            
            while l <= r:
                mid = (l+r) // 2

                if self.store[key][mid][1] == timestamp: 
                    return self.store[key][mid][0]
                elif self.store[key][mid][1] > timestamp:
                    r = mid - 1
                else:
                    l = mid + 1

            return self.store[key][r][0]
 
