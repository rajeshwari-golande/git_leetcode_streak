// Pattern: revise the optimized one
// Difficulty: Hard
// Problem: 668. Kth Smallest Number in Multiplication Table
// Link: https://leetcode.com/problems/kth-smallest-number-in-multiplication-table

class Solution:
    def find_count(self,m,n,value): #finds how many numbers are less than or eq to the value in the matrix
        i=0
        j=n-1
        count=0
        while(i<m and j>=0):
            element=(i+1)*(j+1)
            if element<=value:
                count+=j+1
                i+=1
            else:
                j-=1
        return count

    def findKthNumber(self, m: int, n: int, k: int) -> int:
        low=1
        high=m*n
        while(low<=high):
            mid=(low+high)//2
            count=self.find_count(m,n,mid)
            if count<k:
                low=mid+1
            else:
                high=mid-1
        return low


# optimal-->
# class Solution:
#     def findKthNumber(self, m: int, n: int, k: int) -> int:

#         if m > n:
#             m, n = n, m

#         low = 1
#         high = m * n

#         while low < high:
#             mid = (low + high) // 2

#             count = 0
#             for i in range(1, m + 1):
#                 count += min(mid // i, n)

#             if count < k:
#                 low = mid + 1
#             else:
#                 high = mid

#         return low

        