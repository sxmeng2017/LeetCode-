class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        new_left, new_right = newInterval[0], newInterval[1]
        left_index, right_index = 0, len(intervals) - 1
        res_left_index, res_right_index = -1, -1
        res_left, res_right = -1, -1
        while left_index <= right_index:
            ## 如果要插入的左值在当前区间的左边
            if new_left < intervals[left_index][0]:
                res_left_index, res_left = left_index, new_left
            ## 如果要插入的右值在当前区间的右边
            if new_right > intervals[right_index][1]:
                res_right_index, res_right = right_index, new_right
            ## 如果要插入的左值在当前区间的中间
            if intervals[left_index][0] <= new_left and intervals[left_index][1] >= new_left:
                res_left_index, res_left = left_index, intervals[left_index][0]
            ## 如果要插入的右值在当前区间的中间
            if intervals[right_index][0] <= new_right and intervals[right_index][1] >= new_right:
                res_right_index, res_right = right_index, intervals[right_index][1]
            ## 如果左值右值的位置都找到了
            if res_right_index != -1 and res_left_index != -1:
                break
            ## 如果左值的位置还没找到
            if res_left_index == -1:
                left_index += 1
            ## 如果右值的位置还没找到
            if res_right_index == -1:
                right_index -= 1
        ## 如果最后整个循环完整结束，说明插入区间不和任意一个区间交叉
        if right_index < left_index:
            intervals = intervals[:left_index] + [newInterval] + intervals[left_index:]
            return intervals
        intervals[res_left_index: res_right_index + 1] = [[res_left, res_right]]
        return intervals