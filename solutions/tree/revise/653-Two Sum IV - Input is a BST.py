// Pattern: CHANGE_ME
// Difficulty: Easy
// Problem: 653. Two Sum IV - Input is a BST
// Link: https://leetcode.com/problems/two-sum-iv-input-is-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #two BST iterator solutin pending
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        #iter1 -- > inorder(small to large)
        #iter2--> rev inorder(large to small)
        class BSTiterator:
            def __init__(self,root,reverse=False):
                self.stack=[]
                self.reverse=reverse
                self.pushALL(root)
            def pushALL(self,node):
                while node:
                    self.stack.append(node)
                    #normal inorder--> go left
                    #rev inorder -- >right
                    if self.reverse:
                        node=node.right
                    else:
                        node=node.left
            def next(self):
                #get next node in chosen order
                node=self.stack.pop()
                if self.reverse:
                    self.pushALL(node.left)
                else:
                    self.pushALL(node.right)
                return node.val
            def hasNext(self):
                return len(self.stack)>0
        #smallest val iter
        left_iter=BSTiterator(root)
        right_iter=BSTiterator(root,reverse=True)

        #get inital smallest and largest val
        left=left_iter.next()
        right=right_iter.next()

        #move inwards until iterators meet or cross
        while left<right:
            current_sum=left+right
            if current_sum == k :
                return True
            elif current_sum<k:
                if left_iter.hasNext():
                    left=left_iter.next()
                else:
                    break
            else:
                if right_iter.hasNext():
                    right=right_iter.next()
                else:
                    break
        return False

    # #iterative BFS :
    # def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
    #     if not root:
    #         return False
    #     seen=set()
    #     q=deque([root])
    #     while q:
    #         node=q.popleft()
    #         complement=k-node.val
    #         if complement in seen:
    #             return True
    #         seen.add(node.val)
    #         if node.left:
    #             q.append(node.left)
    #         if node.right:
    #             q.append(node.right)
    #     return False
    

    #recursion DFS-->
    # def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
    #     seen=set()
    #     def dfs(node):
    #         if not node:
    #             return False
    #         complement=k-node.val
    #         if complement in seen:
    #             return True
    #         seen.add(node.val)
    #         return dfs(node.left) or dfs(node.right)
    #     return dfs(root)


# Approach	Time	Auxiliary space	Verdict
# BFS + Set	\(O(n)\)	\(O(n)\)	Excellent, iterative
# DFS + Set	\(O(n)\)	\(O(n)\)	Excellent, concise
# Two BST iterators	\(O(n)\)	\(O(h)\)	Best space efficiency
        