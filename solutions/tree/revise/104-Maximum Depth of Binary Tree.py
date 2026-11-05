// Pattern: CHANGE_ME
// Difficulty: Easy
// Problem: 104. Maximum Depth of Binary Tree
// Link: https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #DFS recurion:
    # def maxDepth(self, root: TreeNode | None) -> int:
    #     if not root:
    #         return 0
    #     return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

    #BFS iterativev:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        q=deque([(root,1)])
        while q:
            node,depth=q.popleft()
            if node.left:
                q.append((node.left,depth+1))
            if node.right:
                q.append((node.right,depth+1))
        return depth

# Approach	Time Complexity	Auxiliary Space	Worst-Case Space
# DFS Recursive	    O(n)	        O(h)	O(n)
# BFS Iterative	    O(n)	        O(w)	O(n)
# n = number of nodes
# h = height of the tree
# w = maximum width of the tree 
        