// Pattern: prefix_Sum
// Difficulty: Medium
// Problem: 974. Subarray Sums Divisible by K
// Link: https://leetcode.com/problems/subarray-sums-divisible-by-k

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        prefix=dict()
        prefix[0]=1
        prefix_value=0
        cnt=0
        for i in range(n):
            prefix_value+=nums[i]
            present_mod=prefix_value%k
            #now-prev=5k --> prev=now-5k or ==> prev mod k = present mod k
            if present_mod in prefix:
                cnt+=prefix[present_mod]
                prefix[present_mod]+=1
            else:
                prefix[present_mod]=1
        return cnt
            



        
        