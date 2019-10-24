class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        for i in A:
            if i % 2 == 0:
                odd.append(i)
            else:
                even.append(i)
        return [i for n in zip(odd, even) for i in n]
