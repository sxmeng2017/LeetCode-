# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        将listnode的值全取出来，排序，再生成有序的链表
        :param head:
        :return:
        """
        temp = []
        root = head
        while root:
            temp.append(root.val)
            root = root.next
        ## 取出值
        temp = sorted(temp)[::-1]
        ## 排序
        root = ListNode(0)
        r = root
        while temp:
            v = temp.pop()
            r.next = ListNode(v)
            r = r.next
        ## 重新生成
        return root.next