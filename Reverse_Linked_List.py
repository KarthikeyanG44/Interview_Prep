class Node:
    def __init__(self,data):
        self.val = data
        self.next = None


class Solution:
    def reverseList(self, head: Node) -> Node:
        if head is None or head.next is None:
            return head

        prev_node = head
        curr_node = head.next

        while (curr_node):
            temp_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp_node
            # print(prev_node.next)
            # print(curr_node.next)
            # print(temp_node.next)

        return prev_node

if __name__=="__main__":
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = None

    s = Solution()
    ans = s.reverseList(head)
    print(ans.val)