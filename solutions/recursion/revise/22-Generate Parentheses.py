// Pattern: nice question
// Difficulty: Medium
// Problem: 22. Generate Parentheses
// Link: https://leetcode.com/problems/generate-parentheses

class Solution:

    def generate(self,open , close , current , ans):
        if open ==0 and close ==0 :
            ans.append(current)
            return 
        if open>0:
            self.generate(open-1,close,current+"(",ans)
        if close>open:
            self.generate(open,close-1,current+")",ans)
        return ans

        
        
        

    def generateParenthesis(self, n: int) -> list[str]:
        #backtracking --> recursion
        ans=list()
        return self.generate(n,n,"",ans)

        