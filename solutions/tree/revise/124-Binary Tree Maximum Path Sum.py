// Pattern: CHANGE_ME
// Difficulty: Hard
// Problem: 124. Binary Tree Maximum Path Sum
// Link: https://leetcode.com/problems/binary-tree-maximum-path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def maxPathSum(self, root: TreeNode | None) -> int:
    #     ans=float('-inf')
    #     def dfs(node):
    #         nonlocal ans
    #         if not node:
    #             return 0
    #         left=max(0,dfs(node.left))
    #         right=max(0,dfs(node.right))
    #         path_sum=left+node.val+right
    #         ans=max(ans,path_sum)
    #         return node.val + max(left,right)
    #     dfs(root)
    #     return ans

    #iterative BFS
    def maxPathSum(self, root: TreeNode | None) -> int:

        if not root:
            return 0

        # Step 1: Perform BFS and store traversal order
        q = deque([root])
        order = []

        while q:
            node = q.popleft()
            order.append(node)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        # Step 2: Store maximum downward gain of each node
        gain = {}

        # Step 3: Initialize global maximum
        ans = float('-inf')

        # Step 4: Process nodes in reverse BFS order
        for node in reversed(order):

            # Get maximum gains from children
            left = max(0, gain.get(node.left, 0))
            right = max(0, gain.get(node.right, 0))

            # Maximum path passing through current node
            path_sum = left + node.val + right

            # Update global maximum
            ans = max(ans, path_sum)

            # Maximum one-sided gain returned upwards
            gain[node] = node.val + max(left, right)

        return ans

# Complexity	Recursive DFS	Iterative BFS + Reverse Processing
# Time Complexity	O(N)	   O(N)
# Auxiliary Space	O(H)	   O(N)
# Traversal	   Postorder DFS	BFS + Reverse order
# Data Structures	Recursion stack	Queue + List + Dictionary