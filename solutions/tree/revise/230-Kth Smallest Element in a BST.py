// Pattern: CHANGE_ME
// Difficulty: Medium
// Problem: 230. Kth Smallest Element in a BST
// Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #BFS with sorting solution:
    # def kthSmallest(self, root: TreeNode | None, k: int) -> int:
    #     if not root:
    #         return None

    #     q = deque([root])
    #     values = []

    #     while q:
    #         node = q.popleft()

    #         values.append(node.val)

    #         if node.left:
    #             q.append(node.left)

    #         if node.right:
    #             q.append(node.right)

    #     values.sort()

    #     return values[k - 1]



    #BFS using heap
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        if not root:
            return None

        q = deque([root])
        max_heap = []

        while q:
            node = q.popleft()
            val = node.val

            if len(max_heap) < k:
                heapq.heappush(max_heap, -val)

            elif val < -max_heap[0]:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, -val)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return -max_heap[0]



    #DFS solution:
    # def kthSmallest(self, root: TreeNode | None, k: int) -> int:
    #     count=0
    #     result=None
    #     if not root:
    #         return None
    #     def inorder(node):
    #         nonlocal count , result
    #         if not node:
    #             return 
    #         inorder(node.left)
    #         count+=1
    #         if count==k:
    #             result=node.val
    #         inorder(node.right)
    #     inorder(root)
    #     return result
             
        
# Approach	                 Time Complexity	    Auxiliary Space Complexity
# BFS + Sorting	                     O(n log n)	    O(n)
# BFS + Max Heap of size k	        O(n log k)	    O(k + w)
# Inorder DFS	                    O(n)	        O(h)
        