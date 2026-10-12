// Pattern: nice logic for reversal , and why cant we reverse while iteration/recursion
// Difficulty: Medium
// Problem: 103. Binary Tree Zigzag Level Order Traversal
// Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #queue solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        q=deque([root])
        result=[]
        lvl=0
        while q:
            level=[]
            for _ in range(len(q)):
                node=q.popleft()
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if lvl%2!=0:
                level=level[::-1]
            result.append(level)   
            lvl+=1
        return result


    #recursion solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        result=[]
        def dfs(node,level):
            if not node:
                return 
            if level==len(result):
                result.append([])
            result[level].append(node.val)

            dfs(node.left,level+1)
            dfs(node.right,level+1)
        dfs(root,0)
        for i in range(len(result)):
            if i%2==1:
                result[i]=result[i][::-1]
        return result

    #time and space complexity = O(n) for both the solutions
            

        