class Node:
    '''
    This class represents a node in the Doubly Linked List
    '''
    def __init__(self, data):
        self.next = None        # pointer to next node
        self.data = data        # the node's data
    
    def __repr__(self):
        return str(self.data)   # a string representation of the node's data

class SinglyLinkedList:
    '''
    This class a Singly Linked List
    
    Basic operations include:
    - insert() -> Adds a node at the beginning of the list
    - deleteAtHead() -> Deletes the node at the beginning of the list
    - insertAfter() -> Inserts a node after a given node
    - delete(node) -> deletes a particular node
    - display() -> Displays the list in natural forward order
    '''
    def __init__(self):
        self.head = None # pointer to the head node

    def clear(self):
        '''
        Function clears entire linked list
        '''
        self.head = None
        print("Linked List has been cleared")

    def display(self):
        '''
        Function to display linked list
        '''
        res = []
        n = self.head
        if n is None:
            print("Linked List is empty")
        else:
            while n is not None:
                res.append(str(n.data))
                n = n.next
            res.append("None")
            print(" -> ".join(res))
    
    def insert(self, data):
        '''
        Function inserts a new node with given data at the head of the linked list
        '''
        n = Node(data)
        if self.head is None:
            self.head = n
            print("Inserted node with key " + str(data) + " as head")
        else:
            n.next = self.head
            self.head = n
            print("Inserted node with key " + str(data))


    def deleteAtHead(self):
        curHead = self.head
        if self.head is None:
            print("ERROR: Linked list is already empty")
        else:
            self.head = self.head.next
            print("Deleted node with key " + str(curHead) + " from head")
    
    def insertAfter(self, key, data):
        '''
        Function inserts a new node with given data AFTER the node with the given key if that node is in the linked list
        '''
        n = Node(data)
        runner = self.head
        if runner is None: # if Linked List is empty cannot insert after any node (none exist...)
            print("ERROR: Node with key", key, "cannot be added because Linked List is empty")
        else: # otherwise insert after the given key
            while runner is not None:   # while we are in bounds
                if runner.data == key: # HIT!
                    n.next = runner.next
                    # if runner.next is None:
                    #     n.next = None
                    runner.next = n
                    print("Inserted node with key", data, "after node with key", key)
                    break # break out of the loop if we have found the key
                elif runner.next is None: # if we are at the tail and we have not found key in the list, print error
                    print("ERROR: Node with key", key, "is not in the Linked List")
                    break
                runner = runner.next
    
    def delete(self, key):
        runner = self.head
        if runner is None:
            self.head = runner.next
        
        while runner.data != key and runner is not None:
            prev = runner
            runner = runner.next
        
        if runner is None:
            print("ERROR: Node with key", key, "is not in the linked list")
            return
        
        prev.next = runner.next