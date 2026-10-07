// Pattern: good question to understand the permutations logic
// Difficulty: Medium
// Problem: 46. Permutations
// Link: https://leetcode.com/problems/permutations

class Solution:

    def find_permutations(self,nums,n,current,ans,used):
        if len(current)==n :
            ans.append(current)
            return

        for j in range(n):
            if not used[j]:
                used[j]=1
                self.find_permutations(nums,n,current+[nums[j]],ans,used)
                used[j]=0
        return ans
    def permute(self, nums: list[int]) -> list[list[int]]:
        used=[0]*len(nums)
        return self.find_permutations(nums,len(nums),[],[],used)

# | Complexity | Answer |
# | **Time** | **O(n × n!)** |
# | **Space (including output)** | **O(n × n!)** |
# | **Auxiliary space** | **O(n)** |