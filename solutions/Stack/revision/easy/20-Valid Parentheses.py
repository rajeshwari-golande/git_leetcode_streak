// Pattern: stack solution 
// Difficulty: Easy
// Problem: 20. Valid Parentheses
// Link: https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        stack=[]
        for i in range(n):
            if stack and ((stack[-1]=='[' and s[i]==']') or (stack[-1]=='(' and s[i]==')') or (stack[-1]=='{' and s[i]=='}')):
                stack.pop()
            else:
                stack.append(s[i])
        if not stack :
            return True
        return False
        