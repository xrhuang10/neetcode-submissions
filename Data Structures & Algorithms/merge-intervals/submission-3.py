class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = [intervals[0]]

        for start, end in intervals:
            endtime = res[-1][1]
            if start <= endtime:
                res[-1][1] = max(end, endtime)
            else:
                res.append([start, end])
        
        return res
