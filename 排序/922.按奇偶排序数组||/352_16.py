class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:

        first, last = 0, len(A) - 1
        while first <= last:
            if A[first] % 2 == 0:
                A[first], A[last] = A[last], A[first]
                last -= 1
            else:
                first += 1
        mid = len(A) // 2
        A[::2], A[1::2] = A[mid:], A[:mid]
        return A