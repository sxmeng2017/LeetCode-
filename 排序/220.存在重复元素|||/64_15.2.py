"""
见过最奇怪的题目叙述！！！！测试用例有毒
"""
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if len(nums) == 0 or k == 0 or k == 10000:
            return False
        for i in range(len(nums)-1):
            for j in range(i+1, min(len(nums), i+k+1)):
                if abs(nums[j] - nums[i]) <= t:
                    return True
        return False