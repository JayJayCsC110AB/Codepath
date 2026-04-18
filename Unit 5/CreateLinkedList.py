class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
class LinkedList:
    # Constructor.
    def __init__(self):
        # The first node in the linked list.
        # The head is either a Node object or None if the list is empty.
        self.head = None

    # Method. Adds a new node with the specific data value to the beginning of the linked list.
    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # Method. Adds a node with specified value to the end of the list.
    def append(self, value):
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        

    # Method. Returns the length of the list.
    def length(self):
        count = 0
        current = self.head
        
        while current:
            count +=1
            current = current.next
        
        return count

    # Method. Returns the value at a given index in the linked list.
    # Index count starts at 0.
    # Returns None if there are fewer nodes in the linked list than the index value.
    def get_at_index(self, index):
        i = 0
        current = self.head
        
        while current:
            if i == index:
                return current.value
            current = current.next
            i+=1
        return None