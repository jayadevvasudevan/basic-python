def insertion_sort(arr):
    """
    Perform an in-place insertion sort on the input list.
    
    Insertion sort works by repeatedly taking the next element from the unsorted portion of the array and inserting it into its correct position in the sorted portion.
    
    Args:
        arr (list): The list to be sorted.
    
    Returns:
        None: The list is sorted in place.
    """
 
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        
        
        while j >= 0 and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        
        
        arr[j + 1] = key_item

# Test cases
if __name__ == "__main__":
    def test_insertion_sort():
        test_cases = [
            ([12, 11, 13, 5, 6, 7], [5, 6, 7, 11, 12, 13]),    # Random order
            ([], []),                                          # Empty array
            ([1], [1]),                                        # Single element
            ([3, 1, 2], [1, 2, 3]),                           # Small array
            ([5, 5, 5, 5], [5, 5, 5, 5]),                     # All elements the same
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),               # Already sorted
            ([9, 7, 5, 3, 1], [1, 3, 5, 7, 9])                # Reverse order
        ]
        
        for i, (input_data, expected) in enumerate(test_cases):
            insertion_sort(input_data)
            assert input_data == expected, f"Test case {i+1} failed: {input_data} != {expected}"
            print(f"Test case {i+1} passed.")
    
    test_insertion_sort()
