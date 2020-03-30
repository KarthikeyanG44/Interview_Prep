# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if not head:
            return None
        if head.next is None and n == 1:
            return None

        count = 0
        countPtr = head
        while (countPtr):
            count += 1
            countPtr = countPtr.next

        if n == count:
            return head.next

        n = n if n < count else n % count

        firstPtr = head
        secondPtr = head.next
        pointerSeparation = 1
        while (pointerSeparation < n):
            secondPtr = secondPtr.next
            pointerSeparation += 1

        while (secondPtr.next):
            firstPtr = firstPtr.next
            secondPtr = secondPtr.next

        firstPtr.next = firstPtr.next.next

        return head