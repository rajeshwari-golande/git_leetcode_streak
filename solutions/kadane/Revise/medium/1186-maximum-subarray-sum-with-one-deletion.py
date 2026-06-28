// Pattern: kadane
// Difficulty: Medium 
// Problem: 1186-maximum-subarray-sum-with-one-deletion.py
// Link: https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n=len(arr)
        one_delete=float(-inf)
        no_delete=float(-inf)
        result=float(-inf)
        for i in range(n):
            prev_one=one_delete
            prev_no=no_delete
            no_delete=max(prev_no+arr[i] , arr[i] )
            if(prev_no == float(-inf)):
                one_delete=max(prev_no,arr[i])    
            else:
                one_delete=max(prev_no,prev_one+arr[i])
            result=max(result,max(no_delete,one_delete))
        return result



        