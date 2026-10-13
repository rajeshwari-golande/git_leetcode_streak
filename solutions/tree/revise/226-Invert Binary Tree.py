// Pattern: CHANGE_ME
// Difficulty: Easy
// Problem: 226. Invert Binary Tree
// Link: https://leetcode.com/problems/invert-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #dfs:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        temp=root.right
        root.right=root.left
        root.left=temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    #bfs
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        q=deque([root])
        while q:
            for _  in range(len(q)):
                node=q.popleft()
                temp=node.right
                node.right=node.left
                node.left=temp
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return root       
                

# Complexity	             DFS (Recursion)	BFS (Queue)
# Time	                     (O(n))	             (O(n))
# Auxiliary space           	(O(h))	         (O(n))
# Worst-case auxiliary space	 (O(n))  	      (O(n))
# Balanced tree space	        (O(log n))    	  (O(n))
        