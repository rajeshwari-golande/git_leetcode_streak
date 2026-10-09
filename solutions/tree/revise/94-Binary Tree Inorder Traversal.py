// Pattern: inorder from bfs input
// Difficulty: Easy
// Problem: 94. Binary Tree Inorder Traversal
// Link: https://leetcode.com/problems/binary-tree-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        result=[]
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)
        inorder(root)
        return result

# TC=O(n) , n=no. of nodes
# SC=(O(h) , h=height of the tree 
