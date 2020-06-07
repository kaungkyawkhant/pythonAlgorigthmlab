class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # function to create new nodes
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        node_data = self.head
        result = []
        while (node_data):
            result.append(str(node_data.data))
            node_data = node_data.next
        return " => ".join(result)

    def reverseList(self):
        current = self.head
        previous = None
        while (current is not None):
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

rlist = LinkedList()
rlist.push(10)
rlist.push(20)
rlist.push(30)
rlist.push(40)
rlist.push(50)
print(rlist.printList())
rlist.reverseList()
print(rlist.printList())
