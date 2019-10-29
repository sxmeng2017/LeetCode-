class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        res = []
        index = len(A)
        while index > 1:
            i = A.index(index)
            A[:i + 1] = A[i::-1]
            res.append(i + 1)
            A[:index] = A[index - 1::-1]
            res.append(index)
            index -= 1
        return res





