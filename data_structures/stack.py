"""Stack

A Last-In-First-Out (LIFO) data structure where elements are added and removed from the top.
Stacks are used in function call management, expression evaluation, backtracking algorithms,
and undo mechanisms.

Time Complexity:
- push: O(1)
- pop: O(1)
- peek: O(1)
- is_empty: O(1)
- size: O(1)

Space Complexity: O(n) where n is the number of elements
"""


class Stack:
    """
    A stack implementation using Python list.
    
    Attributes:
        _items (list): Internal list to store stack elements
        
    Example:
        >>> stack = Stack()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.push(3)
        >>> stack.peek()
        3
        >>> stack.pop()
        3
        >>> stack.size()
        2
    """
    
    def __init__(self):
        """Initialize an empty stack."""
        self._items = []
    
    def push(self, item):
        """
        Add an element to the top of the stack.
        
        Args:
            item: The element to be added to the stack
            
        Returns:
            None
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        Example:
            >>> stack = Stack()
            >>> stack.push(5)
            >>> stack.push(10)
            >>> stack.size()
            2
        """
        self._items.append(item)
    
    def pop(self):
        """
        Remove and return the element at the top of the stack.
        
        Returns:
            The element at the top of the stack
            
        Raises:
            IndexError: If the stack is empty
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        Example:
            >>> stack = Stack()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.pop()
            2
            >>> stack.pop()
            1
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()
    
    def peek(self):
        """
        Return the element at the top of the stack without removing it.
        
        Returns:
            The element at the top of the stack
            
        Raises:
            IndexError: If the stack is empty
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        Example:
            >>> stack = Stack()
            >>> stack.push(42)
            >>> stack.peek()
            42
            >>> stack.size()
            1
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]
    
    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if stack is empty, False otherwise
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        Example:
            >>> stack = Stack()
            >>> stack.is_empty()
            True
            >>> stack.push(1)
            >>> stack.is_empty()
            False
        """
        return len(self._items) == 0
    
    def size(self):
        """
        Return the number of elements in the stack.
        
        Returns:
            int: Number of elements in the stack
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        Example:
            >>> stack = Stack()
            >>> stack.size()
            0
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.size()
            2
        """
        return len(self._items)
    
    def clear(self):
        """
        Remove all elements from the stack.
        
        Returns:
            None
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        Example:
            >>> stack = Stack()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.clear()
            >>> stack.is_empty()
            True
        """
        self._items = []
    
    def __str__(self):
        """
        Return string representation of the stack.
        
        Returns:
            str: String representation showing stack contents
            
        Example:
            >>> stack = Stack()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.push(3)
            >>> print(stack)
            Stack([1, 2, 3])
        """
        return f"Stack({self._items})"
    
    def __repr__(self):
        """
        Return official string representation of the stack.
        
        Returns:
            str: String representation of the stack
        """
        return self.__str__()


if __name__ == "__main__":
    # Test Case 1: Basic push and pop operations
    print("=== Test Case 1: Basic Operations ===")
    stack = Stack()
    print(f"Initial stack: {stack}")
    print(f"Is empty: {stack.is_empty()}")
    
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(f"\nAfter pushing 10, 20, 30: {stack}")
    print(f"Size: {stack.size()}")
    print(f"Peek: {stack.peek()}")
    
    popped = stack.pop()
    print(f"\nPopped element: {popped}")
    print(f"Stack after pop: {stack}")
    print(f"New size: {stack.size()}")
    
    # Test Case 2: Stack with strings
    print("\n=== Test Case 2: String Stack ===")
    string_stack = Stack()
    words = ["Hello", "World", "Python", "Stack"]
    
    for word in words:
        string_stack.push(word)
    print(f"Stack with words: {string_stack}")
    
    print("\nPopping all words (LIFO order):")
    while not string_stack.is_empty():
        print(f"  - {string_stack.pop()}")
    print(f"Empty stack: {string_stack}")
    
    # Test Case 3: Edge cases and error handling
    print("\n=== Test Case 3: Edge Cases ===")
    edge_stack = Stack()
    
    # Test empty stack operations
    try:
        edge_stack.pop()
    except IndexError as e:
        print(f"Expected error on empty pop: {e}")
    
    try:
        edge_stack.peek()
    except IndexError as e:
        print(f"Expected error on empty peek: {e}")
    
    # Test single element
    edge_stack.push(100)
    print(f"\nStack with single element: {edge_stack}")
    print(f"Peek: {edge_stack.peek()}")
    print(f"Size: {edge_stack.size()}")
    
    # Test clear operation
    edge_stack.push(200)
    edge_stack.push(300)
    print(f"Before clear: {edge_stack}")
    edge_stack.clear()
    print(f"After clear: {edge_stack}")
    print(f"Is empty: {edge_stack.is_empty()}")
    
    # Test Case 4: Practical application - Reverse a string
    print("\n=== Test Case 4: Reverse String Application ===")
    def reverse_string(text):
        """Reverse a string using a stack."""
        stack = Stack()
        for char in text:
            stack.push(char)
        
        reversed_text = ""
        while not stack.is_empty():
            reversed_text += stack.pop()
        
        return reversed_text
    
    original = "Hacktoberfest 2025"
    reversed_str = reverse_string(original)
    print(f"Original: {original}")
    print(f"Reversed: {reversed_str}")
    
    # Test Case 5: Balanced parentheses checker
    print("\n=== Test Case 5: Balanced Parentheses Checker ===")
    def is_balanced(expression):
        """Check if parentheses in an expression are balanced."""
        stack = Stack()
        opening = "({["
        closing = ")}]"
        pairs = {')': '(', '}': '{', ']': '['}
        
        for char in expression:
            if char in opening:
                stack.push(char)
            elif char in closing:
                if stack.is_empty() or stack.pop() != pairs[char]:
                    return False
        
        return stack.is_empty()
    
    test_expressions = [
        "()",
        "(()())",
        "({[]})",
        "(()",
        "({[}])",
        "{[(1+2)*(3-4)]}"
    ]
    
    for expr in test_expressions:
        result = "Balanced" if is_balanced(expr) else "Not Balanced"
        print(f"  {expr:20} -> {result}")
    
    print("\n=== All Tests Completed ===")
