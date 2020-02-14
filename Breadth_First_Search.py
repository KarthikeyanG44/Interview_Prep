class Node :
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

def BreadthFirstSearch(root):
    if root is None:
        return
    node_queue = []
    current_node = root
    node_queue.append(current_node)
    while node_queue:
        current_node = node_queue.pop(0)
        if current_node.left is not None:
            node_queue.append(current_node.left)
        if current_node.right is not None:
            node_queue.append(current_node.right)

        print(current_node.data)



if __name__=="__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    BreadthFirstSearch(root)