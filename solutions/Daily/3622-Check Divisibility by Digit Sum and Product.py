// Pattern: CHANGE_ME
// Difficulty: Easy
// Problem: 3622. Check Divisibility by Digit Sum and Product
// Link: https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum=0
        digit_product=1
        for ch in str(n):
            digit_sum+=int(ch)
            digit_product*=int(ch)
        div= n%(digit_sum+digit_product)
        if div==0:
            return True
        return False
        