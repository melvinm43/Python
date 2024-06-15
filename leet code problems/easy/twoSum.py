def two_sum(nums, target):
    # Initialize an empty dictionary to store numbers and their indices
    num_to_index = {}

    # Iterate over the list of numbers with their indices
    for index, num in enumerate(nums):
        # Calculate the complement of the current number
        complement = target - num

        # Check if the complement is already in the dictionary
        if complement in num_to_index:
            # If it exists, return the indices of the complement and the current number
            return [num_to_index[complement], index]

        # Otherwise, store the current number and its index in the dictionary
        num_to_index[num] = index

    # The problem guarantees that there is exactly one solution, so we should not reach this line
    raise ValueError("No two sum solution")

# Example usage:
nums1 = [2, 7, 11, 15]
target1 = 9
print(two_sum(nums1, target1))  # Output: [0, 1]

nums2 = [3, 2, 4]
target2 = 6
print(two_sum(nums2, target2))  # Output: [1, 2]

nums3 = [3, 3]
target3 = 6
print(two_sum(nums3, target3))  # Output: [0, 1]
