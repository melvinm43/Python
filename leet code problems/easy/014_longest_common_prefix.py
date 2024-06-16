"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.


Algorith:

for i < len(str[0])
"""


class Solution(object):
    def longestCommonPrefix(self, word_list: list[str]) -> str:
        """
        :type word_list: List[str]
        :rtype: str
        """
        prefix = ''
        # Loops to iterate on each character in the first word
        for i in range(len(word_list[0])):
            # Loop to iterate oin each word
            for str in word_list:
                if i == len(str) or str[i] !=word_list[0][i]:
                    return prefix
            prefix += word_list[0][i]
        return prefix


wordList1 = ["flower","flow","flight"]
wordList2 = ["dog","racecar","car"]
solution = Solution()
print(solution.longestCommonPrefix(wordList1))
print(solution.longestCommonPrefix(wordList2))

"""
Time Complexity: O(n * m), where n is the number of words and m is the length of the shortest word.
- The outer loop runs up to m times (the length of the shortest word).
- The inner loop runs n times (for each word) for each character of the shortest word.

Space Complexity: O(1), constant space.
- Only a fixed number of variables are used, and the space used for the `prefix` string is proportional to the length of the shortest word.

"""