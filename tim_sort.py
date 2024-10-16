# Tim sort algorithm - default python sort method

MIN_RUN = 32

# Function to perform insertion sort on the array
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Merge function to merge two sorted halves of the array
def merge(arr, left, mid, right):
    len1, len2 = mid - left + 1, right - mid
    left_part, right_part = arr[left:mid + 1], arr[mid + 1:right + 1]
    
    i, j, k = 0, 0, left
    
    while i < len1 and j < len2:
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len2:
        arr[k] = right_part[j]
        j += 1
        k += 1

# Function to return the minimum length of a run from 32 to 64
def min_run_length(n):
    r = 0
    while n >= MIN_RUN:
        r |= n & 1
        n >>= 1
    return n + r

# TimSort function to sort the array
def tim_sort(arr):
    n = len(arr)
    min_run = min_run_length(MIN_RUN)
    
    # Sort individual subarrays of size `min_run` or smaller using insertion sort
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)

    # Start merging from size min_run (or smaller), doubling the size of merged subarrays
    size = min_run
    while size < n:
        for left in range(0, n, size * 2):
            mid = min(n - 1, left + size - 1)
            right = min((left + size * 2 - 1), (n - 1))
            
            if mid < right:
                merge(arr, left, mid, right)

        size *= 2

# Example usage:
if __name__ == "__main__":
    arr = [5, 21, 7, 23, 19, 10, 4, 8, 15, 16, 26, 3]
    print("Original Array:")
    print(arr)
    
    tim_sort(arr)
    
    print("\nSorted Array using TimSort:")
    print(arr)
