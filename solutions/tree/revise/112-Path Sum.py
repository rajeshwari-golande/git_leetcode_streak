// Pattern: CHANGE_ME
// Difficulty: Easy
// Problem: 112. Path Sum
// Link: https://leetcode.com/problems/path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #dfs recursive
    # def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
    #     if not root :
    #         return False
    #     if not root.left and not root.right: #leaf node condition
    #         return root.val==targetSum
    #     remaining=targetSum-root.val
    #     return self.hasPathSum(root.left,remaining) or self.hasPathSum(root.right,remaining)

    #iterative BFS
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False
        q=deque([(root,targetSum)])
        while q:
            node,remaining_sum=q.popleft()
            if not node.left and not node.right:
                if node.val==remaining_sum:
                    return True
            remaining_sum-=node.val
            if node.left:
                q.append((node.left,remaining_sum))
            if node.right:
                q.append((node.right,remaining_sum))

        return False
        
        
# Complexity	        Recursive DFS       	Iterative BFS
# Time	               O(n)	              O(n)
# Space	O             (h)               	O(w)
# Data structure	        Recursion stack 	Queue (deque)
# Worst-case space        	O(n)	        O(n)

        