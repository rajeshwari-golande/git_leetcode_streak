// Pattern: v. imp 
// Difficulty: Easy
// Problem: 572. Subtree of Another Tree
// Link: https://leetcode.com/problems/subtree-of-another-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # #BFS queue solution------>:
    # def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
    #     if not subRoot:
    #         return True
    #     if not root:
    #         return False
        
    #     def isSameTree(node,subnode):
    #         q=deque([(node,subnode)])
    #         while q:
    #             a,b=q.popleft()
    #             if not a and not b:
    #                 continue
    #             if not a or not b:
    #                 return False
    #             if a.val!=b.val:
    #                 return False
    #             q.append((a.left,b.left))
    #             q.append((a.right,b.right))
    #         return True
    #     q=deque([root])
    #     while q:
    #         node=q.popleft()
    #         if node.val==subRoot.val:
    #             if isSameTree(node,subRoot):
    #                 return True
    #         if node.left:
    #             q.append(node.left)
    #         if node.right:
    #             q.append(node.right)
    #     return False
            



    #DFS ---->
    #serialization + KMP (knuth-morris-pratt algo)
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        #preorder dfs serialization:
        def serialize(node):
            result=[]
            def dfs(curr):
                if not curr:
                    result.append("#") #to represent the null values
                    return
                result.append(str(curr.val))
                dfs(curr.left)
                dfs(curr.right)
            dfs(node)
            return result
        
        text=serialize(root)
        pattern=serialize(subRoot)

        #KMP(Knuth-morris=pratt algo) with LPS array(longest proper suffix)
        lps=[0]*len(pattern)
        j=0
        i=1
        while(i<len(pattern)):
            if pattern[j]==pattern[i]:
                j+=1
                lps[i]=j
                i+=1
            elif j>0:
                j=lps[j-1]
            else:
                i+=1

        #search pattern in text using the LPS array:
        i=j=0
        while i<len(text):
            if text[i]==pattern[j]:
                i+=1
                j+=1
                if j==len(pattern):
                    return True
            elif j>0:
                j=lps[j-1]
            else:
                i+=1
        return False


        



    #recursion solution
    # def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
    #     def check(node,subnode):
    #         if not node and not subnode:
    #             return True
    #         if not node or not subnode:
    #             return False
    #         if node.val!=subnode.val:
    #             return False
    #         if node.val==subnode.val:
    #             return check(node.left,subnode.left) and check(node.right,subnode.right)
    #     if not subRoot:
    #         return True
    #     if not root:
    #         return False
    #     if check(root,subRoot):
    #         return True
    #     return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)
        

# Let:
# - \(N\) = number of nodes in root
# - \(M\) = number of nodes in subRoot
# - \(H\) = height of root
# - \(K\) = height of subRoot
# Time and space complexity comparison
# Approach	                            Time complexity (worst case)	       Auxiliary space (worst case)
# 1. DFS + recursive tree comparison	      \(O(NM)\)	                      \(O(H+K)\)
# 2. BFS + BFS tree comparison	              \(O(NM)\)	                      \(O(N+M)\)
# 3. DFS serialization + KMP	              \(O(N+M)\)	                   \(O(N+M)\)

        
        

        