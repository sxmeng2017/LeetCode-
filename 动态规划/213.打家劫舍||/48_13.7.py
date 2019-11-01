class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0
        if len(nums) == 2:
            return max(nums)
        nums1 = nums[:-1]
        nums1[1] = max(nums1[:2])
        # 如果nums1第一个数比第二个大时，需要这样处理才正确
        for i in range(2, len(nums1)):
            nums1[i] = max(nums1[i - 1], nums1[i - 2] + nums1[i])
        nums2 = nums[1:]
        nums2[1] = max(nums2[:2])
        for j in range(2, len(nums2)):
            nums2[j] = max(nums2[j - 1], nums2[j - 2] + nums2[j])
        return max(nums1[-1], nums2[-1])

