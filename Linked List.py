##### Program to implement linked list #####
#### Also contains addition of node at various locations ####

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
    def insertFront(self,newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode
    def insertAfter(self,prevNode, newData):
        newNode = Node(newData)
        newNode.next = prevNode.next
        prevNode.next = newNode

    def insertLast(self,newData):
        newNode = Node(newData)
        last = self.head
        while (last.next):
            last = last.next
        last.next = newNode

    def printNthNode(self,n):
        refPtr = self.head
        mainPtr = self.head
        count = 1
        while (count <= n):
            refPtr = refPtr.next

        while (refPtr.next != None):
            mainPtr = mainPtr.next
            refPtr = refPtr.next

        print(mainPtr.data)


if __name__=="__main__":
    head = Node(3)
    second = Node(4)
    third = Node(5)
    fourth = Node(6)

    listObj = LinkedList()
    head.next = second
    second.next = third
    third.next = fourth
    listObj.head = head

    listObj.insertFront(2)
    listObj.insertAfter(listObj.head.next.next,7)
    listObj.insertLast(20)
    listObj.printList()


