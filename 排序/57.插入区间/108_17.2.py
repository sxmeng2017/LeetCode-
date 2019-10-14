class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x:x[0])
        res = self.merge(intervals)
        return res
    def merge(self, intervals):
        if len(intervals) <= 1:
            return intervals
        res = []
        left, right = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= right:
                if intervals[i][1] > right:
                    right = intervals[i][1]
                else:
                    continue
            else:
                res.append([left, right])
                left, right = intervals[i][0], intervals[i][1]
        res.append([left, right])
        return res