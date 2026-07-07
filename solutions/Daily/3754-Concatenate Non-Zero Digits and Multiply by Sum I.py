// Pattern: CHANGE_ME
// Difficulty: Easy
// Problem: 3754. Concatenate Non-Zero Digits and Multiply by Sum I
// Link: https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x=str()
        sum=0
        for digit in str(n):
            if int(digit)!=0:
                x+=digit
                sum+=int(digit)
        if not x:
            return 0
        return int(x)*sum   
        