// Pattern: stack pattern -- > make list of list 
// Difficulty: Medium
// Problem: 1209. Remove All Adjacent Duplicates in String II
// Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        ans=[]
        for ch in s :
            if stack and stack[-1][0] == ch :
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()    
            else: #if not stack or (stack and stack[-1][0]!=ch):
                stack.append([ch,1])
        
        for ch,count in stack:
            ans+=(ch*count)
        return "".join(ans)
        
        