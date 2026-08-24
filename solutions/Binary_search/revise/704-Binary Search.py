// Pattern: basic
// Difficulty: Easy
// Problem: 704. Binary Search
// Link: https://leetcode.com/problems/binary-search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return -1

            
        