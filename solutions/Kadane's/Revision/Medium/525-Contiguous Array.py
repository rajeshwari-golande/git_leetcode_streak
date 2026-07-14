// Pattern: prefix pattern 
// Difficulty: Medium
// Problem: 525. Contiguous Array
// Link: https://leetcode.com/problems/contiguous-array

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cnt=0
        n=len(nums)
        longest_subarray=0
        prefix=dict()
        prefix[0]=-1
        prefix_value=0
        #try to treat 0 as -1 just for the record and 1 as 1 
        for i in range(n):
            if nums[i]==1:
                prefix_value+=1
            else:
                prefix_value-=1
            if prefix_value in prefix: # indicates that there is a sum of zero in between
                longest_subarray=max(longest_subarray , i-prefix[prefix_value])
            else:
                prefix[prefix_value]=i
        return longest_subarray

                

            
            
        