// Pattern: binary search  pattern , especially finding the optimal way to count in O(N)
// Difficulty: Medium
// Problem: 378. Kth Smallest Element in a Sorted Matrix
// Link: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix

class Solution:

    def find_count(self,matrix,value): #finds number of elements less than the value
        m=len(matrix)
        n=len(matrix[0])
        count=0
        i=0
        j=n-1
        while(i<m and j>=0):
            if matrix[i][j]<=value:
                count+=j+1
                i+=1
            else:
                j-=1
        return count


    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        low=matrix[0][0]
        high=matrix[-1][-1]
        while(low<=high):
            mid=(low+high)//2
            count=self.find_count(matrix,mid)
            if count<k:
                low=mid+1
            else:
                high=mid-1
        return low
        