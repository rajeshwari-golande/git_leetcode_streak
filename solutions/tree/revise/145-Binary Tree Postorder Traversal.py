// Pattern: CHANGE_ME
// Difficulty: Easy
// Problem: 145. Binary Tree Postorder Traversal
// Link: https://leetcode.com/problems/binary-tree-postorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        ans=list()
        def postorder(root):
            if not root:
                return 
            postorder(root.left)
            postorder(root.right)
            ans.append(root.val)
        postorder(root)
        return ans        

# TC=O(n) , n=no. of nodes
# SC=(O(h) , h=height of the tree
