# Definition for singly-linked list.
#### Solution with extra space ####
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return None

        list_ptr = head
        node_list = []
        while list_ptr.next not in node_list and list_ptr.next is not None:
            node_list.append(list_ptr)
            list_ptr = list_ptr.next

        try:
            pos = node_list.index(list_ptr.next)
            return node_list[pos]
        except ValueError:
            return None
##### Solution without extra space ###
## Floyd Cycle Algorithm #####
    def detectCycle(self, head):
        if not head or not head.next or head.next.next is None:
            return None

        first = head.next
        second = head.next.next

        while first != second and second is not None and second.next is not None:
            first = first.next
            second = second.next.next

        if second is None or second.next is None:
            return None

        first = head
        while second != first:
            first = first.next
            second = second.next

        return first