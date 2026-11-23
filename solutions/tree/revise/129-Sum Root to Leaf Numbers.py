// Pattern: CHANGE_ME
// Difficulty: Medium
// Problem: 129. Sum Root to Leaf Numbers
// Link: https://leetcode.com/problems/sum-root-to-leaf-numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #recursive dfs
    # def sumNumbers(self, root: TreeNode | None) -> int:
    #     #newNumber = currentNumber \times 10 + node.val
    #     def dfs(node,sum):
    #         if not node:
    #             return 0
    #         sum=sum*10 + node.val
    #         if not node.left and not node.right: # prevent from adding it twice
    #             return sum
    #         return dfs(node.left,sum) + dfs(node.right,sum)
    #     return dfs(root,0)
            
    #iterative BFS        
    def sumNumbers(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        q=deque([(root,0)])
        ans=0
        while q:
            node,sum=q.popleft()
            sum=sum*10+node.val
            if not node.left and not node.right:
                ans+=sum
            if node.left:
                q.append((node.left,sum))
            if node.right:
                q.append((node.right,sum))
        return ans



# Complexity	Recursive DFS	             Iterative BFS
# Time	            O(N)	                O(N)
# Auxiliary Space	 O(H)	                O(W)
# Data structure	Recursion               stack	Queue (deque)
# Traversal	        Depth-first	                Level-order
# Extra storage	    O(1) per recursive call	                O(1) per queued node