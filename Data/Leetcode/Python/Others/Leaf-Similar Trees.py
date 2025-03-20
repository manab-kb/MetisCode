# https://leetcode.com/problems/leaf-similar-trees/?envType=study-plan-v2&envId=leetcode-75


# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeafs(root, leafs):
            if root:
                if not root.left and not root.right:
                    leafs.append(root.val)
                getLeafs(root.left, leafs)
                getLeafs(root.right, leafs)
            return leafs
        return getLeafs(root1, []) == getLeafs(root2, [])
    
    