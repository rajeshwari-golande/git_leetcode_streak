// Pattern: CHANGE_ME
// Difficulty: Easy
// Problem: 144. Binary Tree Preorder Traversal
// Link: https://leetcode.com/problems/binary-tree-preorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        ans=list()
        def preorder(root):
            if not root:
                return 
            ans.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ans
        