class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first, middle, last = 0, 0, len(nums) - 1
        while middle <= last:
            if nums[middle] == 0:
                nums[middle], nums[first] = nums[first], nums[middle]
                middle += 1
                first += 1
            elif nums[middle] == 1:
                middle += 1
            else:
                nums[middle], nums[last] = nums[last], nums[middle]
                last -= 1
