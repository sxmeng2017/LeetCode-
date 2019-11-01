class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0
        if len(nums) == 2:
            return max(nums)
        length = len(nums)
        nums1 = [0] * length
        nums2 = [0] * length
        nums1[1] = nums[0]
        nums2[1] = nums[1]
        for i in range(2, len(nums)):
            nums1[i] = max(nums1[i-2] + nums[i-1], nums1[i-1])
            nums2[i] = max(nums2[i-2] + nums[i], nums2[i-1])
        return max(nums1[-1], nums2[-1])