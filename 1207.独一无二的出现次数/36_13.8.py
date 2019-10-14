class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
        values = d.values()
        if len(values) == len(set(values)):
            return True
        return False