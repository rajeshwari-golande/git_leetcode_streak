// Pattern: CHANGE_ME
// Difficulty: Easy
// Problem: 111. Minimum Depth of Binary Tree
// Link: https://leetcode.com/problems/minimum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #DFS recursion:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        if not root.left:
            return 1+self.minDepth(root.right)
        if not root.right:
            return 1+self.minDepth(root.left)
        return 1+ min(self.minDepth(root.left) , self.minDepth(root.right))


    #BFS solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        q=deque([(root,1)])
        height=0
        while q:
            node,height=q.popleft()
            if not node.left and not node.right:
                return height
            if  node.left:
                q.append((node.left,height+1))
            if node.right:
                q.append((node.right,height+1))

# Approach	            Time	Auxiliary   Space	Advantage
# DFS Recursion	       O(n)	    O(h)	    Less space for balanced trees
# BFS	                    O(n)	O(w)	    Stops at the nearest leaf
# n = number of nodes
# w = maximum width of the tree
            

        