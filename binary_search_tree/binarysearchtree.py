from binary_search_tree.searchtreenode import Node

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.parent = None
        self.node_location = [] #used for searching node to get list of where node is located, reset after each search
            
    def insert_node(self, value):
        """inserts node based on value to left or right of tree"""
        node = Node(value)
        if self.root is None:
            self.root = node
            self.parent = node
            print(f'Node with data {value} inserted as root.')
            return
    
        else:
            if value < self.parent.data:
                if self.parent.leftChild is None:
                    self.parent.leftChild = node
                    self.parent = self.root #resets self.parent to root after insertion of data
                    print(f'Node with data {value} created. Direction: Left.')
                else:
                    self.parent = self.parent.leftChild
                    return self.insert_node(value)
                    
            elif value > self.parent.data:
                if self.parent.rightChild is None:
                    self.parent.rightChild = node
                    self.parent = self.root #resets self.parent to root after insertion of data
                    print(f'Node with data {value} created. Direction: Right.')
                else:
                    self.parent = self.parent.rightChild
                    return self.insert_node(value)
            elif value == self.parent.data:
                print(f'Node with data {value} already in tree.')

    def search_for_node(self, data, current_node=None):
        """searches for node starting at root of tree""" #could also complete with while loop
        if current_node is None:
            current_node = self.root
            
        if data == current_node.data:
            if data == self.root.data:
                print(f'\nSearching tree for node with data {data}...\n{data} found. Location: [Root of tree]')
            elif data == current_node.data:
                print(f'\nSearching tree for node with data {data}...\n{data} found. Location: {self.node_location}')
        elif data > current_node.data:
            if current_node.rightChild is None:
                print(f'\nSearching tree for node with data {data}...\n{data} not found.')
            else:
                current_node = current_node.rightChild
                self.node_location.append('Right')
                return self.search_for_node(data, current_node)
        elif data < current_node.data:
            if current_node.leftChild is None:
                print(f'\nSearching tree for node with data {data}...\n{data} not found.')
            else:
                current_node = current_node.leftChild
                self.node_location.append('Left')
                return self.search_for_node(data, current_node)
        
        self.node_location = []
    
    def inorder_print_iter(self, current_node=None):
        """left-root-right traversal using iteration"""  
        if current_node is None:
            current_node = self.root
        stack = [] #last in first out
        traverse_print = []
        
        while current_node is not None or stack != []:
            while current_node is not None:
                stack.append(current_node)
                current_node = current_node.leftChild
            current_node = stack.pop()
            traverse_print.append(current_node.data)
            current_node = current_node.rightChild
        
        return traverse_print
    
    def preorder_print_iter(self, current_node=None):
        """root-left-right traversal using iteration"""
        if current_node is None:
            current_node = self.root
        stack = [current_node]
        traverse_print = []
        
        while stack != []:
            current_node = stack.pop()
            traverse_print.append(current_node.data)
            if current_node.rightChild is not None: #adds right child then left child so that popping off last value starts with left child
                stack.append(current_node.rightChild)
            if current_node.leftChild is not None:
                stack.append(current_node.leftChild)
        
        return traverse_print
    
    def inorder_print_recur(self, current_node, traverse_list=None):
        """left-root-right traversal using recursion"""  
        if traverse_list is None:
            traverse_list = []
        
        if current_node is not None:
            self.inorder_print_recur(current_node.leftChild, traverse_list)
            traverse_list.append(current_node.data)
            self.inorder_print_recur(current_node.rightChild, traverse_list)
        
        return traverse_list
    
    def preorder_print_recur(self, current_node, traverse_list=None):
        """root-left-right traversal using recursion"""
        if traverse_list is None:
            traverse_list = []
        
        if current_node is not None:
            traverse_list.append(current_node.data)
            self.preorder_print_recur(current_node.leftChild, traverse_list)
            self.preorder_print_recur(current_node.rightChild, traverse_list)
        
        return traverse_list
    
    def postorder_print_recur(self, current_node, traverse_list=None):
        """left-right-root traversal using recursion"""
        if traverse_list is None:
            traverse_list = []
        
        if current_node is not None:
            self.postorder_print_recur(current_node.leftChild, traverse_list)
            self.postorder_print_recur(current_node.rightChild, traverse_list)
            traverse_list.append(current_node.data)
        
        return traverse_list
        