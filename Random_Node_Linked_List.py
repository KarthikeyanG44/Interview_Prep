# Definition for singly-linked list.

import random
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        count = 0
        curr = head
        self.ll_dict = {}
        while (curr):
            count += 1
            self.ll_dict[count] = curr.val
            curr = curr.next

        self.length = count

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        random_number = random.randint(1, self.length)
        return self.ll_dict[random_number]

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()