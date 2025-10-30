---
name: Data Structures Implementation
about: Implement fundamental data structures in Python
title: '[FEATURE] Implement [Data Structure Name]'
labels: enhancement, good first issue, hacktoberfest
assignees: ''
---

## 📚 Data Structure Implementation Needed

The `data_structures/` folder is currently empty and needs implementations of fundamental data structures in Python.

### 🎯 Objective
Implement a clean, well-documented Python implementation of **[Data Structure Name]**.

### 📋 Requirements

#### Code Quality
- [ ] Clean, readable code following PEP 8 standards
- [ ] Comprehensive docstrings for all classes and methods
- [ ] Type hints where appropriate
- [ ] Clear variable and function names

#### Implementation Details
- [ ] Core functionality implemented correctly
- [ ] Common operations (insert, delete, search, etc.)
- [ ] Edge cases handled properly
- [ ] Time and space complexity documented

#### Documentation
- [ ] Detailed comments explaining the logic
- [ ] Complexity analysis (Big O notation)
- [ ] Usage examples in the main section
- [ ] Test cases demonstrating functionality

#### Testing
- [ ] Multiple test cases included
- [ ] Edge cases tested (empty, single element, large input)
- [ ] Example usage with expected output

### 🔨 Suggested Data Structures to Implement

Choose one or suggest your own:

#### Basic Structures
- [ ] **Stack** - LIFO data structure with push, pop, peek operations
- [ ] **Queue** - FIFO data structure with enqueue, dequeue operations
- [ ] **Linked List** - Singly/Doubly linked list with insert, delete, search
- [ ] **Hash Table** - Hash map with collision handling

#### Tree Structures
- [ ] **Binary Tree** - Basic binary tree with traversals (in-order, pre-order, post-order)
- [ ] **Binary Search Tree (BST)** - With insert, delete, search operations
- [ ] **AVL Tree** - Self-balancing BST
- [ ] **Heap** - Min heap or max heap with heapify operations
- [ ] **Trie** - Prefix tree for string operations

#### Graph Structures
- [ ] **Graph** - Adjacency list/matrix representation
- [ ] **Graph Traversal** - BFS and DFS implementations
- [ ] **Weighted Graph** - For shortest path algorithms

#### Advanced Structures
- [ ] **Segment Tree** - For range queries
- [ ] **Fenwick Tree (Binary Indexed Tree)** - For prefix sums
- [ ] **Disjoint Set (Union-Find)** - With path compression
- [ ] **Red-Black Tree** - Self-balancing BST

### 📝 Implementation Template

```python
"""
[Data Structure Name]
Brief description of the data structure and its use cases.
Time Complexity: 
- Operation1: O(?)
- Operation2: O(?)
Space Complexity: O(?)
"""

class [DataStructureName]:
    """
    [Data Structure] implementation in Python.
    
    Attributes:
        attr1: Description
        attr2: Description
    """
    
    def __init__(self):
        """Initialize the data structure."""
        pass
    
    def operation1(self, param):
        """
        Description of operation.
        
        Args:
            param: Description
        
        Returns:
            Description
        
        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        pass
    
    # Add more methods...
    
    def __str__(self):
        """String representation."""
        pass


# Example usage and test cases
if __name__ == "__main__":
    # Create instance
    ds = [DataStructureName]()
    
    # Test case 1
    print("Test 1: [Description]")
    # ... test code ...
    
    # Test case 2
    print("\nTest 2: [Description]")
    # ... test code ...
    
    # Add more test cases...
```

### 💡 Example: Stack Implementation

See the reference below for what a good implementation looks like:

```python
"""
Stack Data Structure
LIFO (Last In First Out) data structure.
Time Complexity: 
- Push: O(1)
- Pop: O(1)
- Peek: O(1)
Space Complexity: O(n)
"""

class Stack:
    """Stack implementation using a list."""
    
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []
    
    def push(self, item):
        """
        Add an item to the top of the stack.
        
        Args:
            item: Item to add
        
        Time Complexity: O(1)
        """
        self.items.append(item)
    
    def pop(self):
        """
        Remove and return the top item.
        
        Returns:
            The top item
        
        Raises:
            IndexError: If stack is empty
        
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        """
        Return the top item without removing it.
        
        Returns:
            The top item
        
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]
    
    def is_empty(self):
        """Check if stack is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)
    
    def __str__(self):
        """String representation."""
        return f"Stack({self.items})"


# Example usage
if __name__ == "__main__":
    stack = Stack()
    
    # Test push
    print("Pushing: 1, 2, 3")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Stack: {stack}")
    
    # Test peek
    print(f"Top item: {stack.peek()}")
    
    # Test pop
    print(f"Popped: {stack.pop()}")
    print(f"Stack after pop: {stack}")
    
    # Test size
    print(f"Stack size: {stack.size()}")
```

### 📂 File Location
Save your implementation in: `data_structures/[filename].py`

Example filenames:
- `stack.py`
- `queue.py`
- `linked_list.py`
- `binary_search_tree.py`
- `graph_bfs_dfs.py`

### ✅ Acceptance Criteria
- [ ] Code runs without errors
- [ ] All test cases pass
- [ ] Documentation is clear and complete
- [ ] Follows the existing repository structure
- [ ] File is placed in `data_structures/` folder
- [ ] Code is properly formatted (PEP 8)

### 🎃 Hacktoberfest
This issue is part of Hacktoberfest 2024! Contributions are welcome and count towards your Hacktoberfest progress.

### 📌 Notes
- One data structure per pull request
- Check existing PRs to avoid duplicates
- Feel free to implement variations (e.g., circular queue, doubly linked list)
- Add visual diagrams in comments if helpful

### 🤝 How to Contribute
1. Comment on this issue to claim it
2. Fork the repository
3. Create a new branch: `git checkout -b feature/add-[datastructure]`
4. Implement the data structure
5. Test thoroughly
6. Submit a pull request

---

**Looking forward to your contribution! 🚀**
