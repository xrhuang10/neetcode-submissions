class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        before = []
        after = []
        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                before.append(interval)
            elif newInterval[1] < interval[0]:
                after.append(interval)
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        
        answer = []
        answer.extend(before)
        answer.append(newInterval)
        answer.extend(after)
        return answer


