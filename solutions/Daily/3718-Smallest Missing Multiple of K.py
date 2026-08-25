// Pattern: easy peesy
// Difficulty: Easy
// Problem: 3718. Smallest Missing Multiple of K
// Link: https://leetcode.com/problems/smallest-missing-multiple-of-k

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n=k
        while(True):
            if n not in nums:
                return n
            n+=k
        