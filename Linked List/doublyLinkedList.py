class Node:
    def __init__(self, data):
        self.next = None
        self.previous = None
        self.data = data
    
    def __repr__(self):
        return str(self.data)

'''
Following are the basic operations supported by a list.

√  | insertAtHead() -> Insertion − Adds an element at the beginning of the list.
√  | deleteAtHead() -> Deletion − Deletes an element at the beginning of the list.
√  | insertAtTail() -> Insert Last − Adds an element at the end of the list.
√  | deleteAtTail() -> Delete Last − Deletes an element from the end of the list.
√  | insertAfter() -> Insert After − Adds an element after an item of the list.
_  | delete() -> Delete − Deletes an element from the list using the key.
√  | display() -> Display forward − Displays the complete list in a forward manner.
√  | displayReversed() -> Display backward − Displays the complete list in a backward manner.
'''

class LinkedList:
    def __init__(self):
        '''
        Constructor -> initialises the linked list with default head and tail pointing to None
        '''
        self.head = None
        self.tail = None
    
    # def __repr__(self):
    #     '''
    #     Function to return a string representation of the Linked List object
    #     '''
    #     if self.head is None:
    #         return "Linked List is empty"
    #     res = []
    #     node = self.head
    #     res.append("None")
    #     while node != None:
    #         res.append(str(node.data))
    #         node = node.next
    #     res.append("None")
    #     return " <-> ".join(res)

    def display(self):
        '''
        Function prints the linked list in FORWARDS order
        '''
        res = []
        n = self.head
        if n is None:
            print("Linked List is empty")
        else:
            res.append("None")
            while n is not None:
                res.append(str(n.data))
                n = n.next
            res.append("None")
            print(" <-> ".join(res))
    
    def displayReversed(self):
        '''
        Function prints the linked list in REVERSED order
        '''
        res = []
        n = self.tail
        if n is None:
            print("Linked List is empty")
        else:
            res.append("None")
            while n is not None:
                res.append(str(n.data))
                n = n.previous
            res.append("None")
            print(" <-> ".join(res))

    def clearAll(self):
        '''
        Function clears entire linked list
        '''
        self.head = None
        self.tail = None
        print("Linked List has been cleared")

    def insertAtHead(self, data):
        '''
        Function inserts a new node with given data at the head of the linked list
        '''
        # create new Node, set previous to None and next to current head
        n = Node(data)
        n.previous = None
        n.next = self.head # if head is null  (Linked List is empty) then this will set n.next to None either way
        # if the linked list is NOT empty (head is not null) then set current head to point back to new node
        if self.head != None:
            self.head.previous = n
        else:
            # otherwise, set the tail to the new node
            self.tail = n
        # make new node the head
        self.head = n
    
    def deleteAtHead(self):
        '''
        Function deletes the head of the linked list
        '''
        curHead = self.head
        if self.head is not None and self.head.next is not None:
            self.head.next.previous = self.head.previous
            self.head = self.head.next
            print("Deleted node with key " + str(curHead.data) + " at head")
        else:
            self.head = None
            self.tail = None
    
    def insertAtTail(self, data):
        '''
        Function inserts a new node at the tail of the linked list
        '''
        n = Node(data)
        n.next = None
        
        if self.tail is not None:
            self.tail.next = n
            n.previous = self.tail
            self.tail = n
            print("Inserted node with key " + str(data) + " at tail")
        else:
            n.previous = None
            self.head = n
            self.tail = n
    
    def deleteAtTail(self):
        '''
        Function deletes a node at the tail of the linked list
        '''
        curTail = self.tail
        if self.tail is not None and self.tail.previous is not None:
            self.tail.previous.next = self.tail.next
            self.tail = self.tail.previous
            print("Deleted node with key " + str(curTail.data) + " at tail")
        else:
            self.tail = None
            self.head = None

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
                    if runner is not self.tail: # if we are not at the tail, perform the insertion
                        runner.next.previous = n
                        n.next = runner.next
                        runner.next = n
                        n.previous = runner
                        print("Inserted node with key", data, "after node with key", key)
                    else: # we are at the tail, so just do insertion using insertAtTail method
                        self.insertAtTail(data)
                    break # break out of the loop if we have found the key
                elif runner.next is None: # if we are at the tail and we have not found key in the list, print error
                    print("ERROR: Node with key", key, "is not in the Linked List")
                    break
                else:
                    runner = runner.next
    
    def delete(self, key):
        '''
        Function deletes the node with given key from the linked list if it exists
        '''
        runner = self.head
        if runner is None: # if linked list is empty, print error
            print("ERROR: Linked List is already empty")
        else:
            while runner is not None:
                if runner.data == key: # if we found the node to be deleted
                    if runner is self.tail:
                        self.deleteAtTail() # call deleteAtTail method if we are trying to delete the tail element
                    else:
                        runner.previous.next = runner.next
                        runner.next.previous = runner.previous
                    break
                else:
                    runner = runner.next

### TESTING ###

# set up Linked List
ll = LinkedList()
ll.display()

# insert some nodes at head
ll.insertAtHead(1)
ll.insertAtHead(0)
ll.display()

# delete some nodes at head
ll.deleteAtHead()
ll.display()

# insert some nodes at tail
ll.insertAtTail(4)
ll.insertAtTail(3)
ll.display()

# delete some nodes at tail
ll.deleteAtTail()
ll.display()

# add a new node after a particular node
ll.insertAfter(1, 6)
ll.display()

print("--------------------------------")
print("Reversed: ", end="")
ll.displayReversed()
print("--------------------------------")

# clear entire Linked List and confirm it is empty
ll.clearAll()
ll.display()