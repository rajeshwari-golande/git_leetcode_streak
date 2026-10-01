// Pattern: using heap , can be done also using binary search
// Difficulty: Medium
// Problem: 378. Kth Smallest Element in a Sorted Matrix
// Link: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap=[]
        n=len(matrix)
        heap=[]
        ans=0
        cnt=0
        for i in range(n):
            heapq.heappush(heap,(matrix[i][0],i,0)) #push val,row,col
        while heap:
            val,r,c=heapq.heappop(heap)
            cnt+=1
            if cnt==k:
                return val

            if r<n and c<n-1:
                heapq.heappush(heap,(matrix[r][c+1],r,c+1))

#Binary Search approach:
    # def find_count(self,matrix,value): #finds number of elements less than the value
    #     m=len(matrix)
    #     n=len(matrix[0])
    #     count=0
    #     i=0
    #     j=n-1
    #     while(i<m and j>=0):
    #         if matrix[i][j]<=value:
    #             count+=j+1
    #             i+=1
    #         else:
    #             j-=1
    #     return count


    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     low=matrix[0][0]
    #     high=matrix[-1][-1]
    #     while(low<=high):
    #         mid=(low+high)//2
    #         count=self.find_count(matrix,mid)
    #         if count<k:
    #             low=mid+1
    #         else:
    #             high=mid-1
    #     return low
        