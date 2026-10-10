// Pattern: BFS / level order traversal
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
        