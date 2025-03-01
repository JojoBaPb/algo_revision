def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    tries = 0  # Count the number of tries
    
    while left <= right:
        tries += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, tries  # Return index and number of tries
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1, tries  # Target not found

# Example usage
arr = list(range(1, 101))  # List of numbers 1 to 100
target = 83
index, attempts = binary_search(arr, target)
print(f"Target found at index {index} in {attempts} tries.")
