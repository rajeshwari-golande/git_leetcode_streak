// Pattern: CHANGE_ME
// Difficulty: Medium
// Problem: 98. Validate Binary Search Tree
// Link: https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #dfs recursive:
    # def isValidBST(self, root: TreeNode | None) -> bool:
    #     def dfs(node,l,r):
    #         if not node:
    #             return True
    #         if node.val <= l or node.val >=r :
    #             return False
    #         left=dfs(node.left,l,node.val)
    #         right=dfs(node.right,node.val,r)
    #         return left and right
    #     if not root:
    #         return True
    #     return dfs(root,float('-inf'),float('inf'))
    
    #bfs iterative
    def isValidBST(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        q=deque([(root,float('-inf'),float('inf'))])
        while q:
            node,l,r=q.popleft()
            if node.val<=l or node.val>=r:
                return False
            if node.left:
                q.append((node.left,l,node.val))
            if node.right:
                q.append((node.right,node.val,r))
        return True
            
# Complexity	Recursive DFS	Iterative BFS
# Time	\(O(n)\)	\(O(n)\)
# Auxiliary Space	\(O(h)\)	\(O(w)\)
# Data Structure	Recursion stack	Queue (deque)

# Where:
# - \(n\) = total number of nodes.
# - \(h\) = height of the tree.
# - \(w\) = maximum width of the tree.

