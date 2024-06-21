# Definition for a binary tree node.

"""
Complexity Analysis
# Time Complexity O(n):
# The function visits each node exactly once, resulting in O(n) time complexity,
# where n is the number of nodes in the tree.

# Space Complexity O(n):
# 1. Recursion Stack:
#    - The depth of the recursion stack depends on the height of the tree (h).
#    - In the worst case (skewed tree), the height h can be O(n), leading to O(n) space complexity.
#    - In the best case (balanced tree), the height h can be O(log n), leading to O(log n) space complexity.
# 2. Output List:
#    - The output list stores the values of all n nodes, resulting in O(n) space complexity.

# Overall Space Complexity:
# - Worst Case: O(n) for the recursion stack + O(n) for the output list = O(n)
# - Best Case: O(log n) for the recursion stack + O(n) for the output list = O(n)
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root:TreeNode):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


# Function to run the tests
def run_tests():
    sol = Solution()

    # Test case 1: Empty tree
    root = None
    print(sol.inorderTraversal(root))  # Expected output: []

    # Test case 2: Single node tree
    root = TreeNode(1)
    print(sol.inorderTraversal(root))  # Expected output: [1]

    # Test case 3: Tree with multiple nodes
    #       1
    #        \
    #         2
    #        /
    #       3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(sol.inorderTraversal(root))  # Expected output: [1, 3, 2]

    # Test case 4: Full binary tree
    #       4
    #      / \
    #     2   5
    #    / \
    #   1   3
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    print(sol.inorderTraversal(root))  # Expected output: [1, 2, 3, 4, 5]

    # Test case 5: Complete binary tree
    #       4
    #      / \
    #     2   6
    #    / \ / \
    #   1  3 5  7
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    print(sol.inorderTraversal(root))  # Expected output: [1, 2, 3, 4, 5, 6, 7]

# Run the tests
run_tests()
