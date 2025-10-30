"""
Doubly Linked List Data Structure Implementation

A doubly linked list is a linear data structure where each node contains three parts:
1. Data: The value stored in the node
2. Next: Reference to the next node in the sequence
3. Prev: Reference to the previous node in the sequence

This allows bidirectional traversal, making certain operations more efficient.

Time Complexity:
- insert_at_beginning: O(1)
- insert_at_end: O(1)
- insert_at_position: O(n)
- delete_at_beginning: O(1)
- delete_at_end: O(1)
- delete_at_position: O(n)
- search: O(n)
- reverse: O(n)
- display: O(n)
- display_reverse: O(n)

Space Complexity: O(n) where n is the number of nodes
"""

class Node:
    """
    Node class for Doubly Linked List.
    
    Each node contains:
    - data: The value stored in the node
    - next: Reference to the next node
    - prev: Reference to the previous node
    """
    def __init__(self, data):
        """
        Initialize a new node.
        
        Args:
            data: The value to store in the node
        """
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
    Doubly Linked List implementation with bidirectional traversal.
    
    Supports operations:
    - Insert at beginning, end, or any position
    - Delete from beginning, end, or any position
    - Search for elements
    - Reverse the list
    - Display forward and backward
    """
    
    def __init__(self):
        """
        Initialize an empty doubly linked list.
        """
        self.head = None
        self.tail = None
        self.size = 0
    
    def is_empty(self):
        """
        Check if the list is empty.
        
        Returns:
            bool: True if list is empty, False otherwise
            
        Time Complexity: O(1)
        """
        return self.head is None
    
    def insert_at_beginning(self, data):
        """
        Insert a new node at the beginning of the list.
        
        Args:
            data: The value to insert
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = Node(data)
        
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.size += 1
    
    def insert_at_end(self, data):
        """
        Insert a new node at the end of the list.
        
        Args:
            data: The value to insert
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = Node(data)
        
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.size += 1
    
    def insert_at_position(self, data, position):
        """
        Insert a new node at specified position (0-indexed).
        
        Args:
            data: The value to insert
            position: Index where to insert (0 = beginning)
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if position < 0 or position > self.size:
            raise IndexError(f"Invalid position {position}. Valid range: 0-{self.size}")
        
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        if position == self.size:
            self.insert_at_end(data)
            return
        
        new_node = Node(data)
        current = self.head
        
        for _ in range(position - 1):
            current = current.next
        
        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node
        
        self.size += 1
    
    def delete_at_beginning(self):
        """
        Delete the first node from the list.
        
        Returns:
            The data from the deleted node
            
        Raises:
            IndexError: If list is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot delete from empty list")
        
        data = self.head.data
        
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        
        self.size -= 1
        return data
    
    def delete_at_end(self):
        """
        Delete the last node from the list.
        
        Returns:
            The data from the deleted node
            
        Raises:
            IndexError: If list is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot delete from empty list")
        
        data = self.tail.data
        
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        self.size -= 1
        return data
    
    def delete_at_position(self, position):
        """
        Delete node at specified position (0-indexed).
        
        Args:
            position: Index of node to delete
            
        Returns:
            The data from the deleted node
            
        Raises:
            IndexError: If position is invalid
            
        Time Complexity: O(n)
        """
        if position < 0 or position >= self.size:
            raise IndexError(f"Invalid position {position}. Valid range: 0-{self.size-1}")
        
        if position == 0:
            return self.delete_at_beginning()
        
        if position == self.size - 1:
            return self.delete_at_end()
        
        current = self.head
        for _ in range(position):
            current = current.next
        
        data = current.data
        current.prev.next = current.next
        current.next.prev = current.prev
        
        self.size -= 1
        return data
    
    def search(self, data):
        """
        Search for a value in the list.
        
        Args:
            data: The value to search for
            
        Returns:
            int: Position of first occurrence, or -1 if not found
            
        Time Complexity: O(n)
        """
        current = self.head
        position = 0
        
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        
        return -1
    
    def reverse(self):
        """
        Reverse the doubly linked list in place.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if self.is_empty() or self.head == self.tail:
            return
        
        current = self.head
        self.head, self.tail = self.tail, self.head
        
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev
    
    def display(self):
        """
        Display the list from head to tail.
        
        Returns:
            str: String representation of the list
            
        Time Complexity: O(n)
        """
        if self.is_empty():
            return "[]"
        
        elements = []
        current = self.head
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        return " <-> ".join(elements)
    
    def display_reverse(self):
        """
        Display the list from tail to head.
        
        Returns:
            str: String representation of the list in reverse
            
        Time Complexity: O(n)
        """
        if self.is_empty():
            return "[]"
        
        elements = []
        current = self.tail
        
        while current:
            elements.append(str(current.data))
            current = current.prev
        
        return " <-> ".join(elements)
    
    def get_size(self):
        """
        Get the number of nodes in the list.
        
        Returns:
            int: Number of nodes
            
        Time Complexity: O(1)
        """
        return self.size
    
    def __str__(self):
        """String representation of the list."""
        return f"DoublyLinkedList({self.display()})"
    
    def __repr__(self):
        """Developer-friendly representation."""
        return f"DoublyLinkedList(size={self.size})"
    
    def __len__(self):
        """Support for len() function."""
        return self.size


if __name__ == "__main__":
    print("=== Doubly Linked List Implementation ===")
    dll = DoublyLinkedList()
    
    # Test Case 1: Basic insertions
    print("\n=== Test Case 1: Basic Insertions ===")
    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)
    print(f"Forward: {dll.display()}")
    print(f"Backward: {dll.display_reverse()}")
    print(f"Size: {dll.get_size()}")
    
    # Test Case 2: Insert at beginning
    print("\n=== Test Case 2: Insert at Beginning ===")
    dll.insert_at_beginning(5)
    print(f"After inserting 5 at beginning:")
    print(f"Forward: {dll.display()}")
    print(f"Backward: {dll.display_reverse()}")
    
    # Test Case 3: Insert at position
    print("\n=== Test Case 3: Insert at Position ===")
    dll.insert_at_position(15, 2)
    print(f"After inserting 15 at position 2:")
    print(f"Forward: {dll.display()}")
    print(f"Size: {len(dll)}")
    
    # Test Case 4: Deletion operations
    print("\n=== Test Case 4: Deletion Operations ===")
    deleted = dll.delete_at_beginning()
    print(f"Deleted from beginning: {deleted}")
    print(f"Forward: {dll.display()}")
    
    deleted = dll.delete_at_end()
    print(f"Deleted from end: {deleted}")
    print(f"Forward: {dll.display()}")
    
    deleted = dll.delete_at_position(1)
    print(f"Deleted from position 1: {deleted}")
    print(f"Forward: {dll.display()}")
    
    # Test Case 5: Search operation
    print("\n=== Test Case 5: Search Operation ===")
    position = dll.search(20)
    print(f"Position of 20: {position}")
    position = dll.search(99)
    print(f"Position of 99 (not found): {position}")
    
    # Test Case 6: Reverse the list
    print("\n=== Test Case 6: Reverse List ===")
    print(f"Before reverse: {dll.display()}")
    dll.reverse()
    print(f"After reverse: {dll.display()}")
    print(f"Backward after reverse: {dll.display_reverse()}")
    
    # Test Case 7: String data types
    print("\n=== Test Case 7: String Data ===")
    str_dll = DoublyLinkedList()
    str_dll.insert_at_end("Alice")
    str_dll.insert_at_end("Bob")
    str_dll.insert_at_end("Charlie")
    str_dll.insert_at_beginning("Zoe")
    print(f"String list forward: {str_dll.display()}")
    print(f"String list backward: {str_dll.display_reverse()}")
    
    # Test Case 8: Error handling
    print("\n=== Test Case 8: Error Handling ===")
    try:
        empty_dll = DoublyLinkedList()
        empty_dll.delete_at_beginning()
    except IndexError as e:
        print(f"Caught expected error: {e}")
    
    try:
        dll.insert_at_position(100, 999)
    except IndexError as e:
        print(f"Caught expected error: {e}")
    
    print("\n=== All Tests Completed Successfully ===")
    print(f"Final list: {dll}")
