from linked_list.linklist_node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append_node(self, data):
        """appending node with self.tail variable and O(1) - more efficient"""
        node = Node(data)
        
        if self.head is None:
            self.head = node
            self.tail = node
            print(f'Set head of data as {data}.')
            return
        
        else:
            self.tail.next = node
            print(f'Added new node with data {data}.')
            self.tail = self.tail.next #resets new self.tail to newest node
    
    def add_to_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        print(f'Set new head of data as {data}.')
    
    def contains_node(self, data, current_node=None):
        if current_node is None:
            current_node = self.head
        else:
            current_node = current_node
            
        if data != current_node.data:
            if current_node.next is not None:
                current_node = current_node.next
                return self.contains_node(data, current_node)
            else:
                print(f'Node with data {data} not found')
        elif data == current_node.data:
            print(f'Node with data {data} exists')
    
    # def append_node_n(self, data):
    #     """appending node with while loop and O(n) - less efficient"""
    #     node = Node(data)
        
    #     if self.head is None:
    #         self.head = node
    #         return
        
    #     temporary_node = self.head
        
    #     while temporary_node.next is not None:
    #         temporary_node = temporary_node.next
        
    #     temporary_node.next = node