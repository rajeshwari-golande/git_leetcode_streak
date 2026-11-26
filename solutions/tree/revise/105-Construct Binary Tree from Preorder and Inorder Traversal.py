// Pattern: CHANGE_ME
// Difficulty: Medium
// Problem: 105. Construct Binary Tree from Preorder and Inorder Traversal
// Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #recursive dfs
    # def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
    #     # algo:
    #     # 1.Take the first element from preorder. This is the current root.
    #     # 2.Find this root's position in inorder.
    #     # 3.Divide inorder into:
    #     #     - Left portion → left subtree.
    #     #     - Right portion → right subtree.
    #     # 4.Create a TreeNode using the root value.
    #     # 5.Recursively construct the left subtree.
    #     # 6.Recursively construct the right subtree.
    #     # 7.return root
    #     index_map={}#for value,index in inorder
    #     for i,val in enumerate(inorder):
    #         index_map[val]=i
    #     pre_idx=0#for tracking preporder
    #     def dfs(left,right):
    #         nonlocal pre_idx
    #         if left>right:
    #             return None
    #         root_val=preorder[pre_idx]
    #         pre_idx+=1
    #         root=TreeNode(root_val)
    #         mid=index_map[root_val]
    #         root.left=dfs(left,mid-1)
    #         root.right=dfs(mid+1,right)
    #         return root
    #     return dfs(0,len(inorder)-1)

    #Iterative DFS — Stack
    # def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:

    #     if not preorder:
    #         return None

    #     root = TreeNode(preorder[0])
    #     stack = [root]
    #     in_idx = 0

    #     for i in range(1, len(preorder)):

    #         node = TreeNode(preorder[i])

    #         if stack[-1].val != inorder[in_idx]:
    #             # Attach as left child
    #             stack[-1].left = node

    #         else:
    #             # Pop completed nodes
    #             parent = None

    #             while stack and stack[-1].val == inorder[in_idx]:
    #                 parent = stack.pop()
    #                 in_idx += 1

    #             # Attach as right child
    #             parent.right = node

    #         stack.append(node)

    #     return root

    #Iterative BFS — Queue
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:

        if not preorder:
            return None

        # Store inorder indices
        index_map = {val: i for i, val in enumerate(inorder)}

        # Create root
        root = TreeNode(preorder[0])

        # Queue: (node, pre_start, in_start, size)
        queue = deque([(root, 0, 0, len(preorder))])

        while queue:

            node, pre_start, in_start, size = queue.popleft()

            mid = index_map[node.val]

            # Calculate left and right subtree sizes
            left_size = mid - in_start
            right_size = size - left_size - 1

            # Construct left child
            if left_size > 0:
                left_val = preorder[pre_start + 1]
                left_node = TreeNode(left_val)

                node.left = left_node

                queue.append((
                    left_node,
                    pre_start + 1,
                    in_start,
                    left_size
                ))

            # Construct right child
            if right_size > 0:
                right_val = preorder[pre_start + left_size + 1]
                right_node = TreeNode(right_val)

                node.right = right_node

                queue.append((
                    right_node,
                    pre_start + left_size + 1,
                    mid + 1,
                    right_size
                ))

        return root

# Parameter	Recursive DFS	        Iterative DFS (Stack)	Iterative BFS (Queue)
# Building HashMap	\(O(n)\)	        \(O(1)\)	            \(O(n)\)
# Tree construction	\(O(n)\)	         \(O(n)\)	        \(O(n)\)
# Total Time	            \(O(n)\)	        \(O(n)\)	        \(O(n)\)
# Auxiliary space for HashMap	\(O(n)\)	        \(O(1)\)	        \(O(n)\)
# Recursion / Stack / Queue\(O(n)\) recursion	        \(O(n)\) stack	\(O(n)\) queue
# Total Auxiliary Space	\(O(n)\)	            \(O(n)\)	        \(O(n)\)
        