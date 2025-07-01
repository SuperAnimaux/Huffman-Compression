

class Huffman_tree:
    def __init__(self, node, left_child, right_child):
        self.node = node
        self.left_child = left_child #Initialization 
        self.right_child = right_child #Initialization

    def is_a_leaf(self):
        return self.left_child == None and self.right_child == None


    