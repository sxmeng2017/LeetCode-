class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A = sorted(A)
        for i in range(len(A) - 3, -1, -1):
            a, b, c = A[i], A[i+1], A[i+2]
            if a + b > c:
                return a+b+c
        return 0