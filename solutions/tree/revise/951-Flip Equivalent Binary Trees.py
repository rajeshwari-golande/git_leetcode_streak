// Pattern: CHANGE_ME
// Difficulty: Medium
// Problem: 951. Flip Equivalent Binary Trees
// Link: https://leetcode.com/problems/flip-equivalent-binary-trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #BFS-->
    def flipEquiv(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        q=deque([(root1,root2)])
        while q:
            node1,node2=q.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val!=node2.val:
                return False
            left_matches=((not node1.left and not node2.left) or (node1.left and node2.left  and node1.left.val==node2.left.val))
            if left_matches:
                #no flip required
                q.append((node1.left,node2.left))
                q.append((node1.right,node2.right))
            else:
                #there is a flip
                q.append((node1.left,node2.right))
                q.append((node1.right,node2.left))
        return True

    #recursion DFS -->

    # def flipEquiv(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
    #     if not root1 and not root2:
    #         return True
    #     if not root1 or not root2:
    #         return False
    #     if root1.val!=root2.val:
    #         return False
    #     no_flip=self.flipEquiv(root1.left,root2.left) and self.flipEquiv(root1.right,root2.right)
    #     flip=(self.flipEquiv(root1.right,root2.left) and (self.flipEquiv(root1.left,root2.right)))
    #     return no_flip or flip
        

# | Approach        | Time Complexity (Worst Case) | Space Complexity (Worst Case) |
# | --------------- | ---------------------------- | ----------------------------- |
# | DFS (Recursion) | \\(O(n^2)\\)                 | \\(O(n)\\)                    |
# | BFS (Queue)     | \\(O(n)\\)                   | \\(O(n)\\)                    |

#n-->number of nodes in each tree