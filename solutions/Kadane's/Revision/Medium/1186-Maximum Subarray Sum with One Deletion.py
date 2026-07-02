// Pattern: Kadane's
// Difficulty: Medium
// Problem: 1186. Maximum Subarray Sum with One Deletion
// Link: https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n=len(arr)
        no_deletion_sum=float('-inf')
        one_deletion_sum=float('-inf')
        ans=float('-inf')
        for i in range(n):
            one_deletion_sum=max( no_deletion_sum , one_deletion_sum+arr[i])
            no_deletion_sum=max(arr[i],no_deletion_sum+arr[i])
            ans=max(max(ans,no_deletion_sum) , one_deletion_sum)
        return ans


        