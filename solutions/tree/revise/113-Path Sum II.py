// Pattern: CHANGE_ME
// Difficulty: Medium
// Problem: 113. Path Sum II
// Link: https://leetcode.com/problems/path-sum-ii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #dfs recursive:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        if not root:
            return []
        ans=list()
        def path(node,targetSum,way):
            if not node:
                return 
            way.append(node.val)
            if not node.left and not node.right:
                if node.val==targetSum:
                    ans.append(way.copy())
            else:
                remaining=targetSum-node.val
                path(node.left,remaining,way)
                path(node.right,remaining,way)
            way.pop()
        path(root,targetSum,[])
        return ans

    #bfs iterative:
    # def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
    #     if not root:
    #         return []
    #     q=deque([(root,targetSum,[root.val])])
    #     ans=list()
    #     while q:
    #         node,remaining,path=q.popleft()
    #         if not node.left and not node.right:
    #             if remaining==node.val:
    #                 ans.append(path)

    #         else:
    #             remaining-=node.val
    #             if node.left:
    #                 q.append((node.left,remaining,path+[node.left.val]))
    #             if node.right:
    #                 q.append((node.right,remaining,path+[node.right.val]))
    #     return ans

# Complexity	            Recursive DFS + Backtracking	        Iterative BFS + Path Copying
# Time	                     O(n × h)	                                O(n × h)
# Auxiliary Space         	O(h)	                                O(w × h)
# Output Space	            O(k × h)	                                O(k × h)
# Path management	            Shared list using append() and pop()	Independent lists using path + [value]
# Extra list                  copying	Only when saving valid paths	For every child added to queue
        