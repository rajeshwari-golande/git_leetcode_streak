// Pattern: CHANGE_ME
// Difficulty: Easy
// Problem: 543. Diameter of Binary Tree
// Link: https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#dfs recursive:
    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     diameter=0
    #     def dfs(node):
    #         nonlocal diameter
    #         if not node:
    #             return 0
    #         left=dfs(node.left)
    #         right=dfs(node.right)
    #         diameter=max(diameter,left+right)
    #         return 1+max(left,right)
    #     dfs(root)
    #     return diameter
        
#dfs iterative:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        #postorder + stack approach
        stack=[(root,False)]
        heights={}
        diameter=0
        while stack:
            node,visited=stack.pop()
            if not visited:
                #push back as visited
                stack.append((node,True))
                if node.right:
                    stack.append((node.right,False))
                if node.left:
                    stack.append((node.left,False))
            else:
                left_height=heights.get(node.left,0)
                right_height=heights.get(node.right,0)
                diameter=max(diameter,left_height+right_height)
                heights[node]=1+max(left_height,right_height)
        return diameter


# Complexity	Recursive DFS	Iterative DFS
# Time	        O(N)	        O(N)
# Space	        O(H)	        O(N)
# Traversal	    Postorder	    Postorder
# Data str  	Call stack	    Stack + HashMap
            
