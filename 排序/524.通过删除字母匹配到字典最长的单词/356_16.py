class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x: (-len(x), x))
        for word in d:
            i = 0
            for l in s:
                if l == word[i]:
                    i += 1
                if i == len(word):
                    return word
        return ''