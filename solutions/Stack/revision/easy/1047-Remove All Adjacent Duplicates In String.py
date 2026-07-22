// Pattern: stack , note how the stack elements are converted to string again efficiently
// Difficulty: Easy
// Problem: 1047. Remove All Adjacent Duplicates In String
// Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for ch in s: # O(n)
            if stack and stack[-1]==ch:
                stack.pop()
            else:
                stack.append(ch)
        # for character in stack:
        #     ans+=character  --> this takes O(n square for ans+=character so we use join(stack))

        return "".join(stack)
