class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            d[i] = d.get(i, 0) + 1
        value = d.values()
        if len(value) == len(set(value)):
            return True
        return False