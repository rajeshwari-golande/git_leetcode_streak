// Pattern: max heap pattern
// Difficulty: Medium
// Problem: 658. Find K Closest Elements
// Link: https://leetcode.com/problems/find-k-closest-elements

#best solution --> binary search 
#better solution -->heaap


class Point:
    def __init__(self,point):
        self.point=point
    def __lt__(self,other):
        return self.point > other.point



class Solution:

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #max heap for closest(smallest) distance
        heap=[]
        for point in arr:
            dist=abs(x-point)
            heapq.heappush(heap,(-dist,Point(point)))
            # note--> you can also do it like this--> heapq.heappush(heap,(-dist,-point))  
            if len(heap)>k:
                heapq.heappop(heap)
        ans=[x[1].point for x in heap]  
        return sorted(ans)   
