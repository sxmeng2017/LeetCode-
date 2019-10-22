"""
这里的二叉搜索树，从后往前建立树，如果没有比当前值更小的数，就默认0
所以初始化结果全为0，然后每有一个高的就更新结果列表。
"""
class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        self.count = 0


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        length = len(nums)
        root = None
        res = [0 for _ in range(length)]
        ## 初始化，全为0
        for i in reversed(range(length)):
            ## 倒着计算，使插入的数获得已经和后面所有数比较后的结果
            root = self.insertNode(root, nums[i], res, i)
        return res

    def insertNode(self, root, val, res, res_index):
        ## root空的就创建一个结点
        if root == None:
            root = TreeNode(val)
        ## 如果比root的值小就放左子树
        elif val <= root.val:
            root.count += 1
            root.left = self.insertNode(root.left, val, res, res_index)
            ## 递归计算，这里root变为下一层的左子树，保证
            # 不断递归最后添加的数一定在最后，同时左边的树一定比当前根小
            # 右边的树一定比当前根大
        elif val > root.val:
            res[res_index] += root.count + 1
            root.right = self.insertNode(root.right, val, res, res_index)
        return root