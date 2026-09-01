// Pattern: this is not exactly a binary search question , but a similar pattern
// Difficulty: Medium
// Problem: 240. Search a 2D Matrix II
// Link: https://leetcode.com/problems/search-a-2d-matrix-ii

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        low=0
        high=n-1
        while(low<m and high<n and high>=0):
            if matrix[low][high] == target:
                return True
            elif matrix[low][high]<target: #move to bigger elements
                low=low+1
            else:
                high=high-1
        return False

# TC=O(m+n)	
# SC=O(1)



        