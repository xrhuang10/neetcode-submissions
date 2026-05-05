class TimeMap:

    def __init__(self):
        self.hashmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.hashmap.get(key, [])
        l, r = 0, len(values) - 1
        answer = []
        while l <= r:
            m = l + (r-l)//2
            if timestamp >= values[m][0]:
                res = values[m][1]
                l = m + 1
            elif timestamp < values[m][0]:
                r = m - 1
        return res
