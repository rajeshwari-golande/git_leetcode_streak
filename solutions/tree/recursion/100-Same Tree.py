// Pattern: CHANGE_ME
// Difficulty: Easy
// Problem: 100. Same Tree
// Link: https://leetcode.com/problems/same-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q=deque([(p,q)])
        while q:
            x,y=q.popleft()
            if not x and not y:
                continue
            if not x or not y:
                return False
            if x.val!=y.val:
                return False
            q.append((x.left,y.left))
            q.append((x.right,y.right))
        return True

    
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!=q.val:
                return False
            return dfs(p.left,q.left) and dfs(p.right, q.right)
        return dfs(p,q)


# | Approach        | Time Complexity    | Auxiliary Space Complexity                            |
# | --------------- | ------------------ | ----------------------------------------------------- |
# | DFS (Recursive) | \\(O(\min(n,m))\\) | \\(O(\min(h_p,h_q))\\), worst case \\(O(\min(n,m))\\) |
# | BFS (Queue)     | \\(O(\min(n,m))\\) | \\(O(\min(n,m))\\)                                    |

# Where:

# - \\(n, m\\) = number of nodes in trees `p` and `q`.
# - \\(h_p, h_q\\) = heights of trees `p` and `q`.

# Note: These are worst-case bounds for comparing corresponding nodes, with early termination when a mismatch is found. DFS uses the recursion stack, while BFS uses a queue.