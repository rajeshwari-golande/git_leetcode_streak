// Pattern: CHANGE_ME
// Difficulty: Easy
// Problem: 700. Search in a Binary Search Tree
// Link: https://leetcode.com/problems/search-in-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #dfs recursion:
    # def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
    #     if not root:
    #         return None
    #     if root.val==val:
    #         return root
    #     if root.val<val:
    #         return self.searchBST(root.right,val)
    #     else:
    #         return self.searchBST(root.left,val)

    #bfs queue solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        q=deque([root])
        while q:
            node=q.popleft()
            if node.val==val:
                return node
            elif node.val<val and node.right:
                q.append(node.right)
            else:
                if node.left:
                    q.append(node.left)
        return None
        
# | Approach | Time Complexity | Space Complexity |
# | DFS (Recursive) | O(h) | O(h) — Recursion Stack |
# | BFS (Queue) | O(h) | O(1) — Auxiliary Space |

# ### Complexity by BST Structure

# | BST Structure | Time Complexity (Both) | DFS Space | BFS Space |
# |---|---|---|---|
# | Balanced BST | O(log n) | O(log n) | O(1) |
# | Skewed BST | O(n) | O(n) | O(1) |

# Where:
# - n = Number of nodes
# - h = Height of the BST

# Note: The BFS approach uses O(1) auxiliary space because it enqueues at most one child at each step. A conventional BFS that enqueues both children can use O(n) space.
        