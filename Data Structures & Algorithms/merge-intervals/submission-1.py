class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            last = res[-1]
            laststart = last[0]
            lastend = last[1]
            interval = intervals[i]
            newstart = interval[0]
            newend = interval[1]

            if newstart <= lastend:
                res.pop()
                res.append([laststart, max(lastend, newend)])
            else:
                res.append(intervals[i])
        
        return res