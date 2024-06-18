"""
# Binary Search Algorithm:
# 1. Initialize 'left' to 0 and 'right' to len(array) - 1.
# 2. While 'left' <= 'right':
#    a. Calculate 'mid' = (left + right) // 2.
#    b. If array[mid] == target, return 'mid'.
#    c. If array[mid] < target, set 'left' to mid + 1.
#    d. If array[mid] > target, set 'right' to mid - 1.
# 3. If target is not found, return -1.

# Time Complexity: O(log n)
# Space Complexity: O(1)
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) -1
        while left <=right: # important step revise this later
            # mid = (left + right)//2
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid -1 # important step revise this later
            elif target > nums[mid]:
                left = mid + 1 # important step revise this later
        return -1


solution = Solution()

nums = [-1,0,3,5,9,12]
target = 9
print(solution.search(nums,target))