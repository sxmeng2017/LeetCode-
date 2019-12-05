"""
这题中        if not root or not root.left:
            return root
一开始写return None。于是在【0】时报错。本来想分情况写。虽然也行
但感觉不是最简化。而这里直接return root就行。这说明【】，空输入应该有
数据类型的处理。使输出结果数据类型一致（大概）
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root or not root.left:
            return root
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root