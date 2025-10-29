"""
Binary Search Algorithm
Efficiently finds the position of a target value within a sorted array.
Time Complexity: O(log n)
Space Complexity: O(1)
"""

def binary_search(arr, target):
    """
    Perform binary search on a sorted array.
    
    Args:
        arr (list): Sorted list of elements
        target: Element to search for
    
    Returns:
        int: Index of target if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Prevents integer overflow
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_recursive(arr, target, left=0, right=None):
    """
    Recursive implementation of binary search.
    
    Args:
        arr (list): Sorted list of elements
        target: Element to search for
        left (int): Left boundary index
        right (int): Right boundary index
    
    Returns:
        int: Index of target if found, -1 otherwise
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def find_first_occurrence(arr, target):
    """
    Find the first occurrence of target in a sorted array with duplicates.
    
    Args:
        arr (list): Sorted list with possible duplicates
        target: Element to search for
    
    Returns:
        int: Index of first occurrence, -1 if not found
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching in left half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


# Example usage and test cases
if __name__ == "__main__":
    # Test case 1: Standard binary search
    arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]
    target = 23
    result = binary_search(arr, target)
    print(f"Iterative Binary Search: Target {target} found at index {result}")
    
    # Test case 2: Recursive binary search
    target = 45
    result = binary_search_recursive(arr, target)
    print(f"Recursive Binary Search: Target {target} found at index {result}")
    
    # Test case 3: Element not found
    target = 100
    result = binary_search(arr, target)
    print(f"Binary Search: Target {target} found at index {result}")
    
    # Test case 4: First occurrence with duplicates
    arr_with_duplicates = [1, 2, 2, 2, 3, 4, 5, 5, 5, 6]
    target = 5
    result = find_first_occurrence(arr_with_duplicates, target)
    print(f"First occurrence of {target} at index {result}")
    
    # Test case 5: Empty array
    empty_arr = []
    result = binary_search(empty_arr, 5)
    print(f"Binary Search on empty array: {result}")
