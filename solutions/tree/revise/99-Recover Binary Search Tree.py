// Pattern: CHANGE_ME
// Difficulty: Medium
// Problem: 99. Recover Binary Search Tree
// Link: https://leetcode.com/problems/recover-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #dfs recursive:
    # def recoverTree(self, root: TreeNode | None) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #     prev=None#The previously visited node during inorder traversal.
    #     first=None#The first node that is in the wrong position (the larger misplaced value).
    #     second=None#The second node that is in the wrong position (the smaller misplaced value).
    #     def inorder(node):
    #         nonlocal prev,first,second
    #         if not node:
    #             return 
    #         inorder(node.left)
    #         if prev and prev.val > node.val:
    #             if not first:
    #                 first=prev
    #             second=node
    #         prev=node
    #         inorder(node.right)
    #     inorder(root)
    #     first.val,second.val=second.val,first.val
    
    #dfs iterative:
    # def recoverTree(self, root: TreeNode | None) -> None:
    #     stack=[]
    #     curr=root
    #     prev=None
    #     first=None
    #     second=None
    #     while curr or stack:
    #         while curr:
    #             stack.append(curr)
    #             curr=curr.left
    #         curr=stack.pop()
    #         if prev and prev.val > curr.val:
    #             if not first:
    #                 first=prev
    #             second=curr
    #         prev=curr
    #         curr=curr.right
    #     first.val,second.val=second.val,first.val

    #iterative BFS+sorting approach
    def recoverTree(self, root: TreeNode | None) -> None:
        if not root:
            return
        q=deque([root])
        nodes=[]
        while q:
            node=q.popleft()
            nodes.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        def inorder(node,arr):
            if not node:
                return 
            inorder(node.left,arr)
            arr.append(node)
            inorder(node.right,arr)
        original=[]
        inorder(root,original)
        sorted_values=sorted(node.val for node in original)
        first=None
        second=None
        for i in range(len(original)):
            if original[i].val!=sorted_values[i]:
                if not first:
                    first=original[i]
                second=original[i]
        first.val,second.val=second.val,first.val




# Approach              	        Time Complexity	        Auxiliary Space
# Recursive DFS (Inorder)	              \(O(n)\)	         \(O(h)\)
# Iterative DFS (Inorder + Stack)	    \(O(n)\)	        \(O(h)\)
# Iterative BFS + Sorting	            \(O(n\log n)\)	        \(O(n)\)