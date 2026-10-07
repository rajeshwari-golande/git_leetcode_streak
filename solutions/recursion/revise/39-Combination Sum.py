// Pattern: good question
// Difficulty: Medium
// Problem: 39. Combination Sum
// Link: https://leetcode.com/problems/combination-sum

class Solution:
    #we can choose the same element multiple times
    def find_combinations(self,candidates,n,target,current,current_sum,start,ans):
        if current_sum==target:
            ans.append(current)
            return
        if current_sum>target:
            return
        for i in range(start,n):
            self.find_combinations(candidates,n,target,current+[candidates[i]],current_sum+candidates[i],i,ans)
        
        return ans
    
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        return self.find_combinations(candidates,len(candidates),target,[],0,0,[])


# | Complexity | Value |
# |---|---:|
# | **Time** | **O(n^(T/m))** |
# | **Space** | **O(T/m)** auxiliary |
# | **Space including output** | **O(K × T/m)** |
# Where n = number of candidates, T = target, m = smallest candidate, and K = number of valid combinations.