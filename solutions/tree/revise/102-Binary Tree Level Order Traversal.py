// Pattern: Both solutions  -- > for  BFS ---> queue and the recursion
// Difficulty: Medium
// Problem: 102. Binary Tree Level Order Traversal
// Link: https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

#queue solution
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        q = deque([root])
        result = []
        while(q):
            level=[]
            for _ in range(len(q)):
                node=q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right :
                    q.append(node.right)
            result.append(level)
        return result       
# using queue: -->
# Time complexity: (O(n)) — every node is removed from the queue and processed exactly once.
# Space complexity: (O(n)) — the queue can hold nodes from a level, and result stores all node values.



    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        result=[]
        def dfs(node,level):
            if not node:
                return
            if level == len(result):
                result.append([])
            result[level].append(node.val)
            dfs(node.left,level+1)
            dfs(node.right,level+1)
        dfs(root,0)
        return result
# Complexity for recursion
# Time	: (O(n))
# Auxiliary space, excluding output:	(O(h))
# Total space, including output: (O(n))