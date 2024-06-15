"""
Question:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Algorithm:
1. Create an empty hashMap.
2. Loop through the list nums using the enumerate function.
3. For each number, calculate its complement by subtracting the current number from the target value.
4. If the complement exists in the hashMap, return the indices of both the complement and the current number.
5. Update the hashMap with the current number and its index.
"""
def twoSum(nums, target):
    hashMap = {}
    for index,number in enumerate(nums):
        compliment = target - number
        if(compliment in hashMap):
            return [hashMap[compliment],index]
        hashMap[number] =index


numArray = [9,8,6,3,2]
print(twoSum(numArray,8) )

"""
Time Complexity:
The algorithm makes a single pass through the list (O(n)), and each operation within the loop (checking if a key exists, inserting a key-value pair) is done in constant time (O(1)).
Therefore, the overall time complexity is O(n).

Space Complexity:
The hashMap can store up to n elements in the worst case, resulting in a space complexity of O(n).

Summary
Time Complexity: O(n)
Space Complexity: O(n)

"""