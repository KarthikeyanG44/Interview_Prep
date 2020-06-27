# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or head.next is None or head.next.next is None:
            return head

        node_list = []

        curr = head
        length = 1
        while (curr):
            node_list.append(curr)
            curr = curr.next
            length += 1

        count = 1
        curr = head
        while (count < length / 2):
            temp = curr.next
            end_node = node_list.pop()
            curr.next = end_node
            end_node.next = temp
            curr = end_node.next
            count += 1

        curr.next = None

        return head

