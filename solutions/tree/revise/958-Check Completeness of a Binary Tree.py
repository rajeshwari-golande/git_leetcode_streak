// Pattern: CHANGE_ME
// Difficulty: Medium
// Problem: 958. Check Completeness of a Binary Tree
// Link: https://leetcode.com/problems/check-completeness-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #BFS level order
    # def isCompleteTree(self, root: TreeNode | None) -> bool:
    #     if not root:
    #         return True
    #     q=deque([root])
    #     found_null=False
    #     while q:
    #         node=q.popleft()
    #         if not node:
    #             found_null=True
    #         else:
    #             if found_null:
    #                 return False
    #             q.append(node.left)
    #             q.append(node.right)
    #     return True

    #recursive DFS:
    def isCompleteTree(self, root: TreeNode | None) -> bool:
        def count(node):
            if not node:
                return 0
            return 1+count(node.left)+count(node.right)
        total_nodes=count(root)
        
        def dfs(node,index):
            if not node:
                return True
            if index >= total_nodes:
                return False
            left=dfs(node.left,2*index+1)
            right=dfs(node.right,2*index+2)
            return left and right
        return dfs(root,0)


# Complexity	    Iterative BFS	Recursive DFS (Indexing)
# Time	        O(N)	        O(N)
# Auxiliary Space	O(N)	        O(H)
# Data Structure	Queue (deque)	Recursion stack
# Traversals	        1	        2 (Node counting + DFS)


        