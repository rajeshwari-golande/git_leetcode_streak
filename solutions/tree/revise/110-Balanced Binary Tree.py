// Pattern: CHANGE_ME
// Difficulty: Easy
// Problem: 110. Balanced Binary Tree
// Link: https://leetcode.com/problems/balanced-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # A binary tree is height-balanced when, for every node, the height difference between its left and right subtrees is at most 1.

    #DFS recursive:
    # def isBalanced(self, root: TreeNode | None) -> bool:
    #     def height(node):
    #         if not node:
    #             return 0
    #         left=height(node.left)
    #         right=height(node.right)
    #         if (left==(-1) or right==(-1) or abs(left-right)>1):
    #             return -1
    #         return 1+max(left,right)
    #     return height(root)!=(-1)

    #BFS:
    def isBalanced(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        q=deque([root])
        nodes=[]
        while q:
            node=q.popleft()
            nodes.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        #calculate height of subtree bottom up
        heights={}
        for node in reversed(nodes):
            left_height=heights.get(node.left,0)
            right_height=heights.get(node.right,0)
            if abs(left_height-right_height) > 1:
                return False
            heights[node]=1+max(left_height,right_height)
        return True
            
# Approach	Time Complexity	Auxiliary Space	Worst-Case Space
# DFS Recursive	O(n)        	O(h)	O(n)
# BFS Iterative	O(n)	        O(n)	O(n)