// Pattern: max heap pattern
// Difficulty: Medium
// Problem: 973. K Closest Points to Origin
// Link: https://leetcode.com/problems/k-closest-points-to-origin

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #max heap for closest(smallest) distance
        heap=[]
        for point in points:
            # dist=pow((pow(point[0],2)) + (pow(point[1],2)) ,0.5)  comparing root ===> comparing normal val
            dist=(pow(point[0],2)) + (pow(point[1],2)) 
            heapq.heappush(heap,(-dist,point))
            if len(heap)>k:
                heapq.heappop(heap)
        return [x[1] for x in heap]

        