from linked_list.linkedlist import LinkedList
from binary_search_tree.binarysearchtree import BinarySearchTree

#&LinkedListDemo
if __name__ == '__main__':
    print('\n\t***LinkedList Tests***')
    linked_list = LinkedList()

    linked_list.append_node(55)
    linked_list.append_node(60)
    linked_list.append_node(65)
    
    linked_list.add_to_beginning(50)
    
    linked_list.contains_node(55)
    linked_list.contains_node(40)
    
#&Binary search tree demo
if __name__ == '__main__':
    print('\n\t***BST Tests***')
    binary_search_tree = BinarySearchTree()
    
    binary_search_tree.insert_node(100)
    binary_search_tree.insert_node(87)
    binary_search_tree.insert_node(109)
    binary_search_tree.insert_node(90)
    binary_search_tree.insert_node(50)
    binary_search_tree.insert_node(200)
    binary_search_tree.insert_node(50) #double check to see if duplicate can be added
    
    binary_search_tree.search_for_node(50)
    binary_search_tree.search_for_node(100)
    binary_search_tree.search_for_node(109)
    binary_search_tree.search_for_node(88)
    
    bst_inorder = binary_search_tree.inorder_print_iter()
    print(f'\nGathering inorder traverse print using iteration...\n{bst_inorder}')

    bst_inorder_recur = binary_search_tree.inorder_print_recur(binary_search_tree.root)
    print(f'\nGathering inorder traverse print using recursion...\n{bst_inorder_recur}')
    
    bst_preorder = binary_search_tree.preorder_print_iter()
    print(f'\nGathering preorder traverse print using iteration...\n{bst_preorder}')
    
    bst_preorder_recur = binary_search_tree.preorder_print_recur(binary_search_tree.root)
    print(f'\nGathering preorder traverse print using recursion...\n{bst_preorder_recur}')
    
    bst_postorder = binary_search_tree.postorder_print_recur(binary_search_tree.root)
    print(f'\nGathering postorder traverse print using recursion...\n{bst_postorder}')