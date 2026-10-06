// Pattern: nice one 
// Difficulty: Medium
// Problem: 17. Letter Combinations of a Phone Number
// Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def generate(self,i,curr,digits,ans): # i represents the current digit
        mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
        }
        if i==len(digits):
            ans.append(curr)
            return 
        
        for ch in mapping[digits[i]]:
            self.generate(i+1,curr+ch,digits,ans)


        return ans


    def letterCombinations(self, digits: str) -> list[str]:
        ans=[]
        return self.generate(0,"",digits,ans)

        