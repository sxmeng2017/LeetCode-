"""
reverse是这题的精髓所在，如果没有这句，最小和最大两段具有连续性，穿插时可能出现连续是数字
reverse后，最大最小两段的穿插过程没有连续性了，避免了这种情况
"""
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(reverse=True)
        nums[::2], nums[1::2] = nums[len(nums)//2:], nums[:len(nums)//2]