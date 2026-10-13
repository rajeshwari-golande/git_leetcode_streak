// Pattern: CHANGE_ME
// Difficulty: Medium
// Problem: 107. Binary Tree Level Order Traversal II
// Link: https://leetcode.com/problems/binary-tree-level-order-traversal-ii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #queue solution-->BFS
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        result=[]
        q=deque([root])
        while q:
            level=[]
            for _ in range(len(q)):
                node=q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level)
        result=result[::-1]
        return result

    # TC=O(n)
    # SC=O(n)

    #recursion -- >DFS 
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        result=[]
        def dfs(node,level):
            if not node:
                return 
            if level==len(result):
                result.append([])
            result[level].append(node.val)
            dfs(node.left,level+1)
            dfs(node.right,level+1)
        dfs(root,0)
        result=result[::-1]
        return result

    # TC=O(n)
    # SC=O(n+h) ... h=recursion stack



        