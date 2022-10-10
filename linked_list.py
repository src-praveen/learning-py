from dataclasses import dataclass


class Node:
    """
        Single Node
        Has two data attributes data of the node and reference of the next node information
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return f"<Node data: {self.data}>"    


class LinkedList:
    """
        Single Linked list
    """ 
    next_node = None
    def __init__(self):
        self.head = Node

    def is_empty(self):
        return self.head == None

    def size(self):
        """
            Return the number of node in linear time 
            Takes O(n) time
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        Addes a new node containing the data as head of the list
        Takes O(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        '''
            Return the first occurence of the key in the list or `None`
            Takes O(n)
        '''
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node

            return None        

    def __repr__(self):
        """
            String representation of the list
            Take O(n)
        """
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append(f"[Head {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail {current.data}]")
            else:
                nodes.append(f"[{current.data}]")

            current = current.next_node

        return '-> '.join(nodes)        