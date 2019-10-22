class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) < 1:
            return 0
        c = sorted(citations, reverse=True)
        index = 0
        while index < len(c) and c[index] > index:
            index += 1
        return index