class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))

    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array

# class Node:
#   left = property('Node reference or None')
#   right = property('Node reference or None')
#   tag = property('integer')
#
# def do_breadth_first_traversal(binary_tree):
#     '''
#     binary_tree is a reference to a 'node' object with three properties:
#         left  : node
#         right : node
#         tag   : int
#     the left and right properties are references to child nodes.
#     Leaf nodes (the bottom of the (upside-down) tree) have None left and right properties.
#     Visit and return a list of tags in breath-first, left-to-right order.
#     '''
#     tags = []
#     queue = [binary_tree] # add top vertex node into queue to run FIFO
#     while len(queue) > 0:
#         current = queue.pop(0) # move vertex install current variable
#         tags.append(current.tag) # save the tag of current into tags list
#         if current.left is not None: # check if there is child node in left
#             queue.append(current.left)  # if there is child, add it into queue
#             if current.right is not None: # check if there is child node in right
#                 queue.append(current.right) # if there is child, add it into queue
#     return tags
#
#
# test.assert_equals(do_breadth_first_traversal(test_tree), [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
