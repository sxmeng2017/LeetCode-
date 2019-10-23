class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        di = {}
        for index, item in enumerate(d):
            if self.issub(s, item):
                di[item] = (len(item), index)
        res = di.items()
        if len(res) == 0:
            return ""
        res = sorted(res, key=lambda x: (-x[1][0], x[0]))
        return res[0][0]

    def issub(self, s, d):
        i, j = 0, len(s) - 1
        count = 0
        while i <= j and count < len(d):
            if s[i] == d[count]:
                count += 1
            i += 1
        return count == len(d)