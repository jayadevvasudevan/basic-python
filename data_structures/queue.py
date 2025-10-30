"""Queue

A First-In-First-Out (FIFO) data structure where elements are added at the rear and removed from the front.
Queues are used in task scheduling, breadth-first search, printer job management, and handling asynchronous
data transfers.

Time Complexity:
- enqueue: O(1)
- dequeue: O(1)
- front: O(1)
- is_empty: O(1)
- size: O(1)

Space Complexity: O(n) where n is the number of elements
"""


class Queue:
    """
    A queue implementation using Python list.
    
    Attributes:
        _items (list): Internal list to store queue elements
        
    Example:
        >>> queue = Queue()
        >>> queue.enqueue(1)
        >>> queue.enqueue(2)
        >>> queue.enqueue(3)
        >>> queue.front()
        1
        >>> queue.dequeue()
        1
        >>> queue.size()
        2
    """
    
    def __init__(self):
        """Initialize an empty queue."""
        self._items = []
    
    def enqueue(self, item):
        """
        Add an element to the rear of the queue.
        
        Args:
            item: The element to be added to the queue
            
        Returns:
            None
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        Example:
            >>> queue = Queue()
            >>> queue.enqueue(5)
            >>> queue.enqueue(10)
            >>> queue.size()
            2
        """
        self._items.append(item)
    
    def dequeue(self):
        """
        Remove and return the element at the front of the queue.
        
        Returns:
            The element at the front of the queue
            
        Raises:
            IndexError: If the queue is empty
            
        Time Complexity: O(1) amortized
        Space Complexity: O(1)
        
        Example:
            >>> queue = Queue()
            >>> queue.enqueue(1)
            >>> queue.enqueue(2)
            >>> queue.dequeue()
            1
            >>> queue.dequeue()
            2
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)
    
    def front(self):
        """
        Return the element at the front of the queue without removing it.
        
        Returns:
            The element at the front of the queue
            
        Raises:
            IndexError: If the queue is empty
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        Example:
            >>> queue = Queue()
            >>> queue.enqueue(42)
            >>> queue.front()
            42
            >>> queue.size()
            1
        """
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self._items[0]
    
    def rear(self):
        """
        Return the element at the rear of the queue without removing it.
        
        Returns:
            The element at the rear of the queue
            
        Raises:
            IndexError: If the queue is empty
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        Example:
            >>> queue = Queue()
            >>> queue.enqueue(1)
            >>> queue.enqueue(2)
            >>> queue.rear()
            2
        """
        if self.is_empty():
            raise IndexError("rear from empty queue")
        return self._items[-1]
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            bool: True if queue is empty, False otherwise
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        Example:
            >>> queue = Queue()
            >>> queue.is_empty()
            True
            >>> queue.enqueue(1)
            >>> queue.is_empty()
            False
        """
        return len(self._items) == 0
    
    def size(self):
        """
        Return the number of elements in the queue.
        
        Returns:
            int: Number of elements in the queue
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        Example:
            >>> queue = Queue()
            >>> queue.size()
            0
            >>> queue.enqueue(1)
            >>> queue.enqueue(2)
            >>> queue.size()
            2
        """
        return len(self._items)
    
    def clear(self):
        """
        Remove all elements from the queue.
        
        Returns:
            None
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        Example:
            >>> queue = Queue()
            >>> queue.enqueue(1)
            >>> queue.enqueue(2)
            >>> queue.clear()
            >>> queue.is_empty()
            True
        """
        self._items = []
    
    def __str__(self):
        """
        Return string representation of the queue.
        
        Returns:
            str: String representation showing queue contents
            
        Example:
            >>> queue = Queue()
            >>> queue.enqueue(1)
            >>> queue.enqueue(2)
            >>> queue.enqueue(3)
            >>> print(queue)
            Queue([1, 2, 3])
        """
        return f"Queue({self._items})"
    
    def __repr__(self):
        """
        Return official string representation of the queue.
        
        Returns:
            str: String representation of the queue
        """
        return self.__str__()


if __name__ == "__main__":
    # Test Case 1: Basic enqueue and dequeue operations
    print("=== Test Case 1: Basic Operations ===")
    queue = Queue()
    print(f"Initial queue: {queue}")
    print(f"Is empty: {queue.is_empty()}")
    
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(f"\nAfter enqueuing 10, 20, 30: {queue}")
    print(f"Size: {queue.size()}")
    print(f"Front: {queue.front()}")
    print(f"Rear: {queue.rear()}")
    
    dequeued = queue.dequeue()
    print(f"\nDequeued element: {dequeued}")
    print(f"Queue after dequeue: {queue}")
    print(f"New front: {queue.front()}")
    print(f"New size: {queue.size()}")
    
    # Test Case 2: Queue with strings
    print("\n=== Test Case 2: String Queue ===")
    string_queue = Queue()
    names = ["Alice", "Bob", "Charlie", "Diana"]
    
    for name in names:
        string_queue.enqueue(name)
    print(f"Queue with names: {string_queue}")
    
    print("\nDequeuing all names (FIFO order):")
    while not string_queue.is_empty():
        print(f"  - {string_queue.dequeue()}")
    print(f"Empty queue: {string_queue}")
    
    # Test Case 3: Edge cases and error handling
    print("\n=== Test Case 3: Edge Cases ===")
    edge_queue = Queue()
    
    # Test empty queue operations
    try:
        edge_queue.dequeue()
    except IndexError as e:
        print(f"Expected error on empty dequeue: {e}")
    
    try:
        edge_queue.front()
    except IndexError as e:
        print(f"Expected error on empty front: {e}")
    
    try:
        edge_queue.rear()
    except IndexError as e:
        print(f"Expected error on empty rear: {e}")
    
    # Test single element
    edge_queue.enqueue(100)
    print(f"\nQueue with single element: {edge_queue}")
    print(f"Front: {edge_queue.front()}")
    print(f"Rear: {edge_queue.rear()}")
    print(f"Size: {edge_queue.size()}")
    
    # Test clear operation
    edge_queue.enqueue(200)
    edge_queue.enqueue(300)
    print(f"Before clear: {edge_queue}")
    edge_queue.clear()
    print(f"After clear: {edge_queue}")
    print(f"Is empty: {edge_queue.is_empty()}")
    
    # Test Case 4: Practical application - Task scheduling
    print("\n=== Test Case 4: Task Scheduling Simulation ===")
    task_queue = Queue()
    
    # Add tasks
    tasks = [
        "Print document",
        "Send email",
        "Backup files",
        "Update software"
    ]
    
    print("Adding tasks to queue:")
    for task in tasks:
        print(f"  Queued: {task}")
        task_queue.enqueue(task)
    
    print(f"\nTotal tasks in queue: {task_queue.size()}")
    print(f"Next task to execute: {task_queue.front()}")
    
    print("\nExecuting tasks:")
    while not task_queue.is_empty():
        current_task = task_queue.dequeue()
        print(f"  Executing: {current_task}")
        if not task_queue.is_empty():
            print(f"  Next in queue: {task_queue.front()}")
    
    # Test Case 5: Breadth-First Search simulation
    print("\n=== Test Case 5: BFS Level Order Traversal ===")
    
    def bfs_level_order(tree_dict, start):
        """Simulate BFS level order traversal using a queue."""
        if start not in tree_dict:
            return []
        
        queue = Queue()
        visited = []
        queue.enqueue(start)
        
        while not queue.is_empty():
            node = queue.dequeue()
            visited.append(node)
            
            # Add children to queue
            if node in tree_dict:
                for child in tree_dict[node]:
                    queue.enqueue(child)
        
        return visited
    
    # Tree representation: {parent: [children]}
    tree = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': [],
        'E': ['H'],
        'F': [],
        'G': [],
        'H': []
    }
    
    result = bfs_level_order(tree, 'A')
    print(f"Tree structure: {tree}")
    print(f"BFS traversal starting from 'A': {result}")
    print(f"Expected: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']")
    
    print("\n=== All Tests Completed ===")
