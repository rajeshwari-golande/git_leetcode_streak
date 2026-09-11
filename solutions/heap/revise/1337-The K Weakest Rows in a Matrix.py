// Pattern: using heap pattern
// Difficulty: Easy
// Problem: 1337. The K Weakest Rows in a Matrix
// Link: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix

class Solution:
    def find_val(self, mat: List[List[int]]):
        n=len(mat)
        if mat[n-1]==1:
            return n
        if mat[0]==0:
            return 0
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            if mat[mid]==1:
                low=mid+1
            else:
                high=mid-1
        return low

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        #mx heap
        heap=[]
        n=len(mat)
        for i in range(n):
            val=self.find_val(mat[i])
            heapq.heappush(heap,(-val,-i))
            if len(heap)>k:
                heapq.heappop(heap)
        return [index for soldiers, index in sorted((-soldiers, -index) for soldiers, index in heap)]

        