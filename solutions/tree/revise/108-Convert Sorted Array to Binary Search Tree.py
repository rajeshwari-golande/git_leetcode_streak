// Pattern: CHANGE_ME
// Difficulty: Easy
// Problem: 108. Convert Sorted Array to Binary Search Tree
// Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #dfs recursive
    # def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
    #     nums_idx=0
    #     def dfs(left,right):
    #         if left>right:
    #             return None
    #         mid=(left+right)//2
    #         root=TreeNode(nums[mid])
    #         root.left=dfs(left,mid-1)
    #         root.right=dfs(mid+1,right)
    #         return root
    #     return dfs(0,len(nums)-1)


#BFS iterative
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        if not nums:
            return None
        mid=len(nums)//2
        root=TreeNode(nums[mid])
        q=deque([(0,mid-1,root,"left")])
        q.append((mid+1,len(nums)-1,root,"right"))
        while q:
            left,right,parent,direction=q.popleft()
            if left>right:
                continue
            mid=(left+right)//2
            node=TreeNode(nums[mid])
            if direction=="left":
                parent.left=node
            else:
                parent.right=node
            q.append((left,mid-1,node,"left"))
            q.append((mid+1,right,node,"right"))
        return root
            


# Complexity	DFS Recursive	BFS Iterative
# Time Complexity	\(O(n)\)	\(O(n)\)
# Auxiliary Space	\(O(\log n)\)	\(O(n)\)
# Recursion Stack	\(O(\log n)\)	\(O(1)\)
# Queue Space	\(O(1)\)	\(O(n)\)
# Output Tree Space	\(O(n)\)	\(O(n)\)
# Overall Space (including output)	\(O(n)\)	\(O(n)\)

        