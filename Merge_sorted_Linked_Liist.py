# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 0->2->3->4, 2->9->18

# Output: 0 -> 2 -> 2-> 3 -> 4 -> 5 -> 8

class Node:
    def __init__(self, data):
        self.val = data 
        self.next = None 

def merge_sorted_linked_list(head_1, head_2):
    # Create a new dummy node
    temp_start_node = Node(-1)
    current_node = temp_start_node
    list_1_ptr = head_1
    list_2_ptr = head_2
#     Think of how this will work for one of them empty, both empty, other cases

    while list_1_ptr and list_2_ptr:
        if list_1_ptr.val < list_2_ptr.val :
            current_node.next = list_1_ptr
            list_1_ptr = list_1_ptr.next
            current_node = list_1_ptr
        else :
            current_node.next = list_2_ptr
            list_2_ptr = list_2_ptr.next
            current_node = list_2_ptr

    current_node.next = list_1_ptr or list_2_ptr 

    return temp_start_node.next

#     Garbage collection - Java
#     If you create memory, you have to delete it - Memory leak

# Think of this later
def merge_sorted_linked_list(head_1, head_2):

    if head_1 is None or head_2 or None:
        return head_1 or head_2

    if head_1.val < head_2.val:
        head_1.next = merge_sorted_linked_list(head_1.next, head_2)
        return head_1
    else:
        head_2.next = merge_sorted_linked_list(head_1, head_2.next)
        return head_2
