// Pattern:nice question to learn how to traverse from start to end
// Difficulty: Medium
// Problem: 131. Palindrome Partitioning
// Link: https://leetcode.com/problems/palindrome-partitioning

class Solution:

    def solve(self,s,start,n,current,ans):
        if start==n :
            ans.append(current)
            return
        for end in range(start,n):
            temp=s[start:end+1]
            if temp==temp[::-1]:
                self.solve(s,end+1,n,current+[temp],ans)
        return ans
            
            


    def partition(self, s: str) -> list[list[str]]:
        #backtracking -->recursion
        n=len(s)
        return self.solve(s,0,n,[],[])
        