// Pattern: CHANGE_ME
// Difficulty: Medium
// Problem: 235. Lowest Common Ancestor of a Binary Search Tree
// Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #dfs recursion:
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     if p.val<root.val and q.val<root.val:
    #         return self.lowestCommonAncestor(root.left,p,q)
    #     if p.val>root.val and q.val>root.val:
    #         return self.lowestCommonAncestor(root.right,p,q)
    #     return root


    #BFS iterative:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val and q.val<root.val :
                root=root.left
            elif p.val>root.val and q.val>root.val:
                root=root.right
            else:
                return root
        return None  

    # #BFS queue:
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     queue=deque([root])
    #     while queue:
    #         node=queue.popleft()
    #         if node.val<p.val and node.val<q.val :
    #             if node.right:
    #                 queue.append(node.right)
    #         elif node.val>p.val and node.val>q.val:
    #             if node.left:
    #                 queue.append(node.left)
    #         else:
    #             return node
    #     return None



### Complexity Comparison

# | Approach | Time | Space |
# |---|---|---|
# | DFS (Recursive) | O(h) | O(h) |
# | Iterative (Single Variable) | O(h) | O(1) |
# | Iterative (Queue) | O(h) | O(1) |

# **Where:**
# - `n` = Number of nodes
# - `h` = Height of the BST

# **For a balanced BST:**
# - Time: O(log n)
# - DFS space: O(log n)
# - Iterative space: O(1)

# **For a skewed BST:**
# - Time: O(n)
# - DFS space: O(n)
# - Iterative space: O(1)

# **Note:** The queue approach uses O(1) space because it adds at most one child per iteration.
        