"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        charMap = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
            }
        stack = []
        for char in s:
            if char in charMap: # Checking the character is  Closing Bracket:
                # checks if the stack is not empty and if the top of the stack matches the corresponding opening bracket
                if stack and stack[-1] == charMap[char]:
                    stack.pop() # Indicating a valid matching pair.
                else:
                    # If the stack is empty or the top of the stack does not match the corresponding opening bracket
                    return False
            else: # It means char is an opening bracket
                stack.append(char)
        # If the stack is empty, it means all the opening brackets have been matched and closed properly
        return True if not stack else False



#s[i+1] == charMap[s[i]] or

s1 = "(]" #False
s2 = "()[]{}" #True
s3 = "()" #True
s4 = "()[{}" #False
s5 = "{[]}" #True
s6 = "){" #False
s7 = "({{{{}}}))" #False
s8 = "{[]}" #True

solution = Solution()
if(solution.isValid(s1) == False ): print("S1 Test Passed")
else: "S1 Failed"
if(solution.isValid(s2) == True ): print("S2 Test Passed")
else: "S2 Failed"
if(solution.isValid(s3) == True ): print("S3 Test Passed")
else: "S3 Failed"
if(solution.isValid(s4) == False ): print("S4 Test Passed")
else: "S4 Failed"
if(solution.isValid(s5) == True ): print("S5 Test Passed")
else: "S5 Failed"
if(solution.isValid(s6) == False ): print("S6 Test Passed")
else: "S6 Failed"
if(solution.isValid(s7) == False): print("S7 Test Passed")
else: "S7 Failed"
if (solution.isValid(s8) == True): print("S8 Test Passed")
else: "S8 Failed"
