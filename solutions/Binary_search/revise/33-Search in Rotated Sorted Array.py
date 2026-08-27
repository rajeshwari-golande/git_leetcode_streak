// Pattern: nice pattern for understanding the sorted side
// Difficulty: Medium
// Problem: 33. Search in Rotated Sorted Array
// Link: https://leetcode.com/problems/search-in-rotated-sorted-array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans=-1
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif(nums[mid]>nums[high]): #definitely a dip to the right -->means left side is sorted
                if nums[mid]>target and nums[low]<=target:
                    high=mid-1
                else:
                    low=mid+1
            else:#nums[mid]<=nums[high]-->normal trend -->means right side is sorted
                if nums[mid]<target and target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return ans
        