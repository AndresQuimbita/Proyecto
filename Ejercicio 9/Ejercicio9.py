'''
9. Given a Circular Linked List node, which is sorted in ascending order, write a function to insert a value insertVal into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.
If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.

If the list is empty (i.e., the given node is null), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the originally given node.

Example 1:

Input: head = [3,4,1], insertVal = 2
Output: [3,4,1,2]
Explanation: In the figure above, there is a sorted circular list of three elements. You are given a reference to the node with value 3, and we need to insert 2 into the list. The new node should be inserted between node 1 and node 3. After the insertion, the list should look like this, and we should still return node 3.
'''

class Node:
    """
    Implementation of a node
    """

    def __init__(self, val=None, next_Node=None):
        self.val = val
        self.next_node = next_Node

    def set_next_node(self, next_node):
        self.next_node = next_node


class SinglyLinkedList:
    """
    Implementation of a singly linked list
    """

    def __init__(self, head_node=None):
        self.head_node = head_node

    def list_traversed(self):
        node = self.head_node
        while node:
            print(node.val)
            node = node.next_node
            if node.val == self.head_node.val:
                break

    def append(self, data):
        """
        Insert a node at the end of the list
        """
        if self.head_node is None:
            new_node = Node(data)
            self.head_node = new_node
            return
        node = self.head_node
        while node.next_node:
            node = node.next_node
        new_node = Node(data)
        node.next_node = new_node


def array_to_list(head):
    '''
    Convert a python list to a Circular Linked list
    '''
    list_array = SinglyLinkedList()
    for i in head:
        list_array.append(i)
    node = list_array.head_node
    while node:
        if node.next_node == None:
            node.next_node = list_array.head_node
            break
        node = node.next_node
    return list_array


def insert_Value(head, insert):
    '''
    Insert a value in a Cirular Linked List
    '''
    if not head:
        return [insert]
    list_array = array_to_list(head)
    if(list_array.head_node is None):
        list_array.head_node = Node(insert, None)
        list_array.head_node.next = list_array.head_node
        return list_array.head_node
    cur = list_array.head_node
    while cur:
        if(cur.val < cur.next_node.val):
            if(cur.val <= insert and insert <= cur.next_node.val):
                cur.next_node = Node(insert, cur.next_node)
                break
        else:
            if(cur.val > cur.next_node.val):
                if(cur.val <= insert or insert <= cur.next_node.val):
                    cur.next_node = Node(insert, cur.next_node)
                    break
            else:
                if(cur.next_node == list_array.head_node):
                    cur.next_node = Node(insert, list_array.head_node)
                    break
        cur = cur.next_node

    '''
    Convert a Circular Linked List to a python list an return it
    '''
    node = list_array.head_node
    array = []
    while node:
        array.append(node.val)
        node = node.next_node
        if node.val == list_array.head_node.val:
            break
    return array
