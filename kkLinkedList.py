class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        result = []
        while node is not None:
            result.append(node.data)
            node = node.next
        result.append("None")
        return " => ".join(result)

linkedList = LinkedList()

first_node = Node('a')
linkedList.head = first_node

second_node = Node('p')
third_node = Node('p')
fourth_node = Node('l')
fifth_node = Node('e')

first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node
fourth_node.next = fifth_node

print(linkedList)