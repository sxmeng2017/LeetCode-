from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s = set(nums)
        if len(s) == 1 and 0 in s:
            return '0'
        nums = sorted([str(n) for n in nums], key=cmp_to_key(self.strCmp), reverse=True)
        return "".join(nums)

    def strCmp(self, x1, x2):
        if x1 + x2 > x2 + x1:
            return 1
        return -1