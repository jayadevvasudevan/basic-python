from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    # Sort the input array
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        # Skip duplicate values for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, n - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum < 0:
                left += 1  # We need a larger sum
            elif current_sum > 0:
                right -= 1  # We need a smaller sum
            else:
                # Found a triplet
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for the second number
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for the third number
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1
    
    return result

# Example usage
if __name__ == "__main__":
    test_input = [-1, 0, 1, 2, -1, -4]
    print("Input:", test_input)
    print("Unique Triplets that sum to zero:", threeSum(test_input))
