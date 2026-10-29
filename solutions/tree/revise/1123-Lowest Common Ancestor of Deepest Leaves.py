// Pattern: CHANGE_ME
// Difficulty: Medium
// Problem: 1123. Lowest Common Ancestor of Deepest Leaves
// Link: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def lcaDeepestLeaves(self, root: TreeNode | None) -> TreeNode | None:
    #     def dfs(node):
    #         if not node:
    #             return (0,node)
    #         left_depth,left_lca=dfs(node.left)
    #         right_depth,right_lca=dfs(node.right)
    #         if left_depth==right_depth:
    #             #current node is the lca
    #             return (left_depth+1,node)
    #         elif left_depth>right_depth:
    #             return (left_depth+1,left_lca)
    #         else:
    #             return (right_depth+1,right_lca)
    #     depth,ans=dfs(root)
    #     return ans

#BFS iterative -- > 
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        q = deque([root])
        parent = {root: None}
        deepest = []

        #  BFS to find the deepest level
        while q:
            deepest = []

            for _ in range(len(q)):
                node = q.popleft()

                #  Add node to deepest
                deepest.append(node)

                #  Process left and right children
                if node.left:
                    parent[node.left]=node
                    q.append(node.left)
                if node.right:
                    parent[node.right]=node
                    q.append(node.right)

        #  Move deepest nodes upward
        # A set removes duplicate ancestors automatically
        candidates=set(deepest)
        while len(candidates)>1:
            candidates={parent[node] for node in candidates}
        return candidates.pop()


# Complexity	Recursive DFS	Iterative BFS
# Time	\(O(n)\)	\(O(n)\)
# Auxiliary space	\(O(h)\)	\(O(n)\)
# Balanced tree space	\(O(\log n)\)	\(O(n)\)
# Skewed tree space	\(O(n)\)	\(O(n)\)
# Extra data structures	Recursion stack	Queue, parent dictionary, deepest list, candidate sets
        
        