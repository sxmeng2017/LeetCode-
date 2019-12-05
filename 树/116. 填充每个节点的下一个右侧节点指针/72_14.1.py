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
        if not root:
            return
        stack = [root]
        temp_stack = []
        temp_node = None
        flag = 0
        while stack:
            if flag == 0:
                ## 广度优先遍历
                for node in stack:
                    if node.left:
                        temp_stack.append(node.left)
                    if node.right:
                        temp_stack.append(node.right)
                flag = 1
            ## 队列内节点前后连接
            after = stack.pop()
            # print(after.val)
            after.next = temp_node
            temp_node = after
            if not stack:
                temp_node = None
                stack = temp_stack
                temp_stack = []
                flag = 0
        return root
