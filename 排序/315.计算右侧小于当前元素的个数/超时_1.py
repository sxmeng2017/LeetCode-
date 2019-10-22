class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if len(nums) < 1:
            return []
        res = []
        for i in range(len(nums) -1):
            count = 0
            for j in range(i+1, len(nums)):
                if nums[j] >= nums[i]:
                    continue
                count += 1
            res.append(count)
        res.append(0)
        return res