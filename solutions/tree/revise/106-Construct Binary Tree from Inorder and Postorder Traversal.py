// Pattern: CHANGE_ME
// Difficulty: Medium
// Problem: 106. Construct Binary Tree from Inorder and Postorder Traversal
// Link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
    #     index_map={}
    #     for i,val in enumerate(inorder):
    #         index_map[val]=i
    #     post_idx=len(postorder)-1
    #     def dfs(left,right):
    #         nonlocal post_idx
    #         if left>right:
    #             return None
    #         root_val=postorder[post_idx]
    #         post_idx-=1
    #         root=TreeNode(root_val)
    #         mid=index_map[root_val]
    #         root.right=dfs(mid+1,right)
    #         root.left=dfs(left,mid-1)
    #         return root
    #     return dfs(0,len(inorder)-1)
            
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:

            if not inorder:
                return None

            # Step 1: Store inorder indices
            index_map = {val: i for i, val in enumerate(inorder)}

            # Step 2: Create root (last element of postorder)
            n = len(postorder)
            root = TreeNode(postorder[n - 1])

            # Step 3: Initialize queue
            # (node, post_start, in_start, size)
            queue = deque([(root, 0, 0, n)])

            # Step 4: Process subtrees level by level
            while queue:

                node, post_start, in_start, size = queue.popleft()

                # Find root position in inorder
                mid = index_map[node.val]

                # Calculate subtree sizes
                left_size = mid - in_start
                right_size = size - left_size - 1

                # Construct left subtree
                if left_size > 0:

                    left_val = postorder[post_start + left_size - 1]
                    left_node = TreeNode(left_val)

                    node.left = left_node

                    queue.append((
                        left_node,
                        post_start,
                        in_start,
                        left_size
                    ))

                # Construct right subtree
                if right_size > 0:

                    right_val = postorder[post_start + size - 2]
                    right_node = TreeNode(right_val)

                    node.right = right_node

                    queue.append((
                        right_node,
                        post_start + left_size,
                        mid + 1,
                        right_size
                    ))

            return root
    
# Criteria	                Recursive DFS	                    Iterative BFS
# Time efficiency	                \(O(n)\)	                    \(O(n)\)
# Space efficiency	                \(O(n)\)	                    \(O(n)\)
# Code simplicity             	Easier	                             More bookkeeping
# Recursion overhead	                Yes                 	            No
# HashMap required	                Yes	                              Yes
# Interview preference	        Higher	                    Lower for this problem