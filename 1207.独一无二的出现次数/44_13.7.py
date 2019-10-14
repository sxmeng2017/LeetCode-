class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
        if len(d.values()) == len(set(d.values())):
            return True
        return False