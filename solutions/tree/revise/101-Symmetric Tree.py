// Pattern: CHANGE_ME
// Difficulty: Easy
// Problem: 101. Symmetric Tree
// Link: https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#queue
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        q=deque([(root.left,root.right)])
        while q:
            left,right=q.popleft()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val!=right.val:
                return False
            q.append((left.left,right.right))
            q.append((left.right,right.left))
        return True

#recursion
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        def mirror(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val!=right.val:
                return False
            return ( mirror(left.left,right.right) and mirror(left.right,right.left))
        return mirror(root.left,root.right)
        

# | Approach        | Time Complexity | Auxiliary Space Complexity                                                 |
# | --------------- | --------------- | -------------------------------------------------------------------------- |
# | DFS (Recursive) | (O(n))          | (O(h)), where \\(h\\) is the height of the tree; worst case \\(O(n)\\) |
# | BFS (Queue)     | (O(n))          |  (O(n)) in the worst case                                               |

# Note: \\(n\\) = number of nodes in the binary tree. DFS uses the recursion stack, while BFS uses a queue to store pairs of mirror nodes.