// Pattern: Prefix_sum
// Difficulty: Medium --> v.v.imp
// Problem: 560. Subarray Sum Equals K
// Link: https://leetcode.com/problems/subarray-sum-equals-k

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        prefix_sum=dict()
        value=0
        prefix_sum[0]=1
        cnt=0
        i=0
        for i in range(n):
            value+=nums[i]
            n1=value-k
            if prefix_sum.get(n1)!=None:
                cnt+=prefix_sum[n1]
            prefix_sum[value]=prefix_sum.get(value,0)+1
            
        return cnt


        