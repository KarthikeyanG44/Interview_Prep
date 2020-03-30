
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def __init__(self):
        self.existingNodes = dict()  #### Gives a mapping between old and new nodes/linked list

    def findRandomNode(self, node):
        if node:
            if node in self.existingNodes:
                return self.existingNodes[node]
            else:
                self.existingNodes[node] = Node(node.val, None, None)
                return self.existingNodes[node]
        return None

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        if (head.next is None and head.random is None):
            return Node(head.val, None, None)

        newHead = Node(head.val, None, None)
        self.existingNodes[head] = newHead
        curr = newHead
        old = head
        while (old):
            curr.next = self.findRandomNode(old.next)
            curr.random = self.findRandomNode(old.random)
            old = old.next
            curr = curr.next

        return newHead