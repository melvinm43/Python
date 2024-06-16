"""
9. Palindrome Number
Easy
Topics
Companies
Hint
Given an integer x, return true if x is a
palindrome
, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-231 <= x <= 231 - 1
"""

"""
Algorithm:
1. If number is less than 0 then its not a palindrome , because negative numbers cannot be a palindrome, 
   so return false
2. Initialise reverse  = 0
3. find last_digit , last_digit = num % 10
4. reverse = (reverse * 10) + last_digit
5. num = num // 10
5. call isPalindrome(num,reverse) -> Recursive call
"""
class Solution():
    def isPalindrome(self, num):
        def reverse_num(num):
            reverse = 0
            while num > 0:
                last_digit = num % 10
                reverse = (reverse * 10) + last_digit
                num = num // 10
            return reverse
        if num < 0:
            return False
        elif reverse_num(num) == num:
            return True
        else:
            return False
# Example usage
solution = Solution()
print(solution.isPalindrome(121))  # Output: True
print(solution.isPalindrome(-121))  # Output: False
print(solution.isPalindrome(10))  # Output: False
print(solution.isPalindrome(1221))  # Output: True

"""
1. **Time Complexity:** O(log10(n))
   - The nested function `reverse_num` iterates over each digit of the number, 
     which takes logarithmic time relative to the number of digits.
   - In terms of Big-O notation, it is O(log10(n)), where `n` is the value of the number.

2. **Space Complexity:** O(1)
   - The function uses a constant amount of extra space for variables like `reverse` and `last_digit`.
   - Thus, the space complexity is constant, O(1).

### Comparison of Complexity Values:

### Time Complexity (in increasing order):
- O(1): Constant Time
- O(log n): Logarithmic Time (The above function's time complexity O(log10(n)) fits here)
- O(n): Linear Time
- O(n log n): Linearithmic Time
- O(n^2): Quadratic Time
- O(n^3): Cubic Time
- O(2^n): Exponential Time
- O(n!): Factorial Time

### Space Complexity (in increasing order):
- O(1): Constant Space (The above function's space complexity O(1) fits here)
- O(log n): Logarithmic Space
- O(n): Linear Space
- O(n log n): Linearithmic Space
- O(n^2): Quadratic Space
- O(n^3): Cubic Space
- O(2^n): Exponential Space
- O(n!): Factorial Space

### Conclusion:
- The `isPalindrome` function is efficient in terms of both time and space, with a logarithmic time complexity and constant space complexity.
"""