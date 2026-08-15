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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1+max(self.maxDepth(root.right),self.maxDepth(root.left))
#BFS:
        # q=deque([root])
        # level=0
        # while q:
        #     n=len(q)
        #     for i in range(n):
        #         node=q.popleft()
        #         if node.left:    
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level+=1
        # return level



        
        