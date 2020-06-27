import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Node:
    def __init__(self, node):
        self.val = node.val
        self.next = node.next

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val

    def __gt__(self, other):
        return self.val > other.val

    def return_node(self):
        return self.val, self.next


class Solution:
    def convert_node_to_list_node(self, node):
        val, node_next = node.return_node()
        new_list_node = ListNode(val)
        new_list_node.next = node_next
        return new_list_node

    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        new_list = [Node(node) for node in lists]

        temporary_head = Node(ListNode(-1))
        prev_node = temporary_head
        heapq.heapify(new_list)
        while (new_list):
            min_node = new_list.pop(0)
            prev_node.next = min_node
            min_node = min_node.next
            if min_node:
                min_node = Node(min_node)
                heapq.heappush(new_list, min_node)
            else:
                heapq.heapify(new_list)
            prev_node = prev_node.next

        new_head = temporary_head.next
        # new_head = self.convert_node_to_list_node(new_head)
        curr_node = new_head
        while (curr_node):
            curr_node = self.convert_node_to_list_node(curr_node)
            curr_node = curr_node.next

        return new_head

if __name__ == "__main__":
    l1node1 = ListNode(1)
    l1node2 = ListNode(4)
    l1node3 = ListNode(5)
    l1node1.next = l1node2
    l1node2.next = l1node3

    l2node1 = ListNode(1)
    l2node2 = ListNode(3)
    l2node3 = ListNode(4)
    l2node1.next = l2node2
    l2node2.next = l2node3

    l3node1 = ListNode(2)
    l3node2 = ListNode(6)
    l3node1.next = l3node2

    s = Solution()
    merged_head = s.mergeKLists([l1node1,l2node1,l3node1])
    print(merged_head)

