# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        temp1 = headA
        temp2 = headB

        A_set = set()
        B_set = set()

        while temp1 and temp2:
            A_set.add(temp1)
            B_set.add(temp2)

            if temp1 in B_set:

                return temp1
            elif temp2 in A_set:

                return temp2

            temp1 = temp1.next
            temp2 = temp2.next

        if temp1:
            while temp1:
                if temp1 in B_set:
                    return temp1

                temp1 = temp1.next

        if temp2:
            while temp2:
                if temp2 in A_set:
                    return temp2

                temp2 = temp2.next

        return None