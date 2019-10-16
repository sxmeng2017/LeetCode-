class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                nums = nums[:i] + nums[i+1:]
                nums.insert(0, 0)
            elif nums[i] == 2:
                nums = nums[:i] + nums[i+1:]
                nums.append(2)
            else:
                continue
        nums = nums


"""
思路没问题，但有巨大的问题就是i会从0到length-1，
但是每次删除添加会改变每个i此时的值，会把没必要重复操作的值
再次操作一次。应该每将一个值放最后，整体遍历长度就少1.

至于提交不能的原因，应该是nums[:i] + nums[i+1:]，
这句相当于创建了新的存储空间存新值。而原来存值的位置内的数据没变
"""