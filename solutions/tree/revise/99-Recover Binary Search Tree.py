// Pattern: CHANGE_ME
// Difficulty: Medium
// Problem: 99. Recover Binary Search Tree
// Link: https://leetcode.com/problems/recover-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev=None#The previously visited node during inorder traversal.
        first=None#The first node that is in the wrong position (the larger misplaced value).
        second=None#The second node that is in the wrong position (the smaller misplaced value).
        def inorder(node):
            nonlocal prev,first,second
            if not node:
                return 
            inorder(node.left)
            if prev and prev.val > node.val:
                if not first:
                    first=prev
                second=node
            prev=node
            inorder(node.right)
        inorder(root)
        first.val,second.val=second.val,first.val
        