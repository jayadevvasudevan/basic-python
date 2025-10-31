"""Singly Linked List

A linear data structure where elements (nodes) are connected via references (pointers).
Each node contains data and a reference to the next node in the sequence.
Linked lists are used in dynamic memory allocation, implementing stacks/queues,
and when frequent insertions/deletions are needed.

Time Complexity:
- insert_at_beginning: O(1)
- insert_at_end: O(n)
- insert_at_position: O(n)
- delete: O(n)
- search: O(n)
- get_size: O(1)

Space Complexity: O(n) where n is the number of nodes
"""


class Node:
    """Node class representing an element in the linked list."""
    
    def __init__(self, data):
        """
        Initialize a node with data and no next reference.
        
        Args:
            data: The value to store in the node
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    Singly Linked List implementation.
    
    Attributes:
        head (Node): Reference to the first node in the list
        _size (int): Number of nodes in the list
    
    Example:
        >>> ll = LinkedList()
        >>> ll.insert_at_end(1)
        >>> ll.insert_at_end(2)
        >>> ll.insert_at_end(3)
        >>> ll.display()
        [1, 2, 3]
    """
    
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
        self._size = 0
    
    def is_empty(self):
        """
        Check if the linked list is empty.
        
        Returns:
            bool: True if empty, False otherwise
            
        Time Complexity: O(1)
        """
        return self.head is None
    
    def get_size(self):
        """
        Return the number of nodes in the list.
        
        Returns:
            int: Number of nodes
            
        Time Complexity: O(1)
        """
        return self._size
    
    def insert_at_beginning(self, data):
        """
        Insert a new node at the beginning of the list.
        
        Args:
            data: Value to insert
            
        Time Complexity: O(1)
        
        Example:
            >>> ll = LinkedList()
            >>> ll.insert_at_beginning(5)
            >>> ll.display()
            [5]
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1
    
    def insert_at_end(self, data):
        """
        Insert a new node at the end of the list.
        
        Args:
            data: Value to insert
            
        Time Complexity: O(n)
        
        Example:
            >>> ll = LinkedList()
            >>> ll.insert_at_end(10)
            >>> ll.insert_at_end(20)
            >>> ll.display()
            [10, 20]
        """
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self._size += 1
    
    def insert_at_position(self, data, position):
        """
        Insert a new node at a specific position.
        
        Args:
            data: Value to insert
            position (int): Position to insert at (0-indexed)
            
        Raises:
            IndexError: If position is invalid
            
        Time Complexity: O(n)
        """
        if position < 0 or position > self._size:
            raise IndexError(f"Invalid position: {position}")
        
        if position == 0:
            self.insert_at_beginning(data)
        elif position == self._size:
            self.insert_at_end(data)
        else:
            new_node = Node(data)
            current = self.head
            for _ in range(position - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self._size += 1
    
    def delete(self, data):
        """
        Delete the first occurrence of a node with given data.
        
        Args:
            data: Value to delete
            
        Raises:
            ValueError: If data not found
            
        Time Complexity: O(n)
        """
        if self.is_empty():
            raise ValueError("Cannot delete from empty list")
        
        if self.head.data == data:
            self.head = self.head.next
            self._size -= 1
            return
        
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        
        if current.next is None:
            raise ValueError(f"Value {data} not found in list")
        
        current.next = current.next.next
        self._size -= 1
    
    def search(self, data):
        """
        Search for a value in the list.
        
        Args:
            data: Value to search for
            
        Returns:
            int: Index of the value, or -1 if not found
            
        Time Complexity: O(n)
        """
        current = self.head
        index = 0
        
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        
        return -1
    
    def get(self, index):
        """
        Get the value at a specific index.
        
        Args:
            index (int): Index to retrieve
            
        Returns:
            The data at the specified index
            
        Raises:
            IndexError: If index is out of bounds
            
        Time Complexity: O(n)
        """
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of range")
        
        current = self.head
        for _ in range(index):
            current = current.next
        
        return current.data
    
    def reverse(self):
        """
        Reverse the linked list in place.
        
        Time Complexity: O(n)
        
        Example:
            >>> ll = LinkedList()
            >>> for i in [1, 2, 3]: ll.insert_at_end(i)
            >>> ll.reverse()
            >>> ll.display()
            [3, 2, 1]
        """
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def display(self):
        """
        Return a list representation of the linked list.
        
        Returns:
            list: List of all values in order
            
        Time Complexity: O(n)
        """
        result = []
        current = self.head
        
        while current:
            result.append(current.data)
            current = current.next
        
        return result
    
    def __str__(self):
        """String representation of the linked list."""
        return str(self.display())


if __name__ == "__main__":
    # Test Case 1: Basic operations
    print("=== Test Case 1: Basic Operations ===")
    ll = LinkedList()
    print(f"Empty list: {ll.display()}")
    print(f"Is empty: {ll.is_empty()}")
    
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    print(f"\nAfter inserting 10, 20, 30: {ll.display()}")
    print(f"Size: {ll.get_size()}")
    
    # Test Case 2: Insert at beginning and position
    print("\n=== Test Case 2: Insert Operations ===")
    ll.insert_at_beginning(5)
    print(f"After insert at beginning (5): {ll.display()}")
    
    ll.insert_at_position(15, 2)
    print(f"After insert 15 at position 2: {ll.display()}")
    print(f"Size: {ll.get_size()}")
    
    # Test Case 3: Search and get
    print("\n=== Test Case 3: Search and Get ===")
    value = 20
    index = ll.search(value)
    print(f"Search for {value}: found at index {index}")
    print(f"Value at index 2: {ll.get(2)}")
    
    # Test Case 4: Delete operations
    print("\n=== Test Case 4: Delete Operations ===")
    ll.delete(15)
    print(f"After deleting 15: {ll.display()}")
    print(f"Size: {ll.get_size()}")
    
    # Test Case 5: Reverse
    print("\n=== Test Case 5: Reverse ===")
    print(f"Before reverse: {ll.display()}")
    ll.reverse()
    print(f"After reverse: {ll.display()}")
    
    # Test Case 6: Edge cases
    print("\n=== Test Case 6: Edge Cases ===")
    edge_ll = LinkedList()
    
    try:
        edge_ll.delete(10)
    except ValueError as e:
        print(f"Expected error on empty delete: {e}")
    
    edge_ll.insert_at_end(100)
    print(f"Single element list: {edge_ll.display()}")
    
    try:
        edge_ll.get(5)
    except IndexError as e:
        print(f"Expected error on invalid index: {e}")
    
    # Test Case 7: Practical example - Detect cycle (bonus)
    print("\n=== Test Case 7: String List ===")
    name_list = LinkedList()
    names = ["Alice", "Bob", "Charlie", "Diana"]
    
    for name in names:
        name_list.insert_at_end(name)
    
    print(f"Names list: {name_list.display()}")
    print(f"Search for 'Charlie': index {name_list.search('Charlie')}")
    
    name_list.delete("Bob")
    print(f"After deleting 'Bob': {name_list.display()}")
    
    print("\n=== All Tests Completed ===")
