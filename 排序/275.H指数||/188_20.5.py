class Solution:
    def hIndex(self, citations: List[int]) -> int:
        index = 0
        while index < len(citations) and citations[len(citations) - index - 1] > index:
            index += 1
        return index