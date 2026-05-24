class TimeMap:

    def __init__(self):
        self.hashmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.hashmap:
            self.hashmap[key] = []
        
        self.hashmap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        list_of_values = self.hashmap.get(key, [])
        l = 0
        r = len(list_of_values) - 1
        answer = ''
        while l <= r:
            m = l + (r-l)//2
            if list_of_values[m][0] <= timestamp:
                answer = list_of_values[m][1]
                l = m + 1
            else: 
                r = m - 1
        
        return answer
        


        
