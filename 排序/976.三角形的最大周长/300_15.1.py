class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A = sorted(A)
        m = 0
        for i in range(len(A)-2):
            a, b, c = A[i:i+3]
            if a + b > c:
                if a + b+ c > m:
                    m = a+b+c
            else:
                continue
        return m