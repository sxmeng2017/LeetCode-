class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        res = []
        intervals = sorted(intervals, key=lambda x: x[0])
        left = intervals[0][0]
        right = intervals[0][1]
        for i in range(1, len(intervals)):
            ## 重叠
            if intervals[i][0] <= right:
                if intervals[i][1] > right:
                    right = intervals[i][1]
                else:
                    continue
            ## 不重叠
            if intervals[i][0] > right:
                res.append([left, right])
                left, right = intervals[i][0], intervals[i][1]
        res.append([left, right])
        return res




