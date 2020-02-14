### Inorder Traversal ###

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


def in_order(root):

    if root:
        in_order(root.left)

        print(root.data)

        in_order(root.right)

def pre_order(root):

    if root:
        print(root.data)
        pre_order(root.left)
        pre_order(root.right)


def post_order(root):

    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data)


if __name__=="__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Inorder traversal of the tree")
    in_order(root)
    print("Pre order traversal of tree")
    pre_order(root)
    print("Post Order traversal of tree")
    post_order(root)
