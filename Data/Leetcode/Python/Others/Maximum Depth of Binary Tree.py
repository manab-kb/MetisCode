# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        else:
            lChild = root.left
            rChild = root.right
            
            return 1 + max(self.maxDepth(lChild), self.maxDepth(rChild))
        

"""
Tree of 

    1
   / \
  2   3
 / \
4   5
"""

node4 = TreeNode(4)
node5 = TreeNode(5)
node2 = TreeNode(2)
node2.left = node4
node2.right = node5
node3 = TreeNode(3)
root = TreeNode(1)
root.left = node2
root.right = node3

solution = Solution()
depth = solution.maxDepth(root)
print(depth)
