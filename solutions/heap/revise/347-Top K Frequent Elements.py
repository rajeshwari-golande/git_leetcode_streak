// Pattern: top k freq --> pair heap pattern
// Difficulty: Medium
// Problem: 347. Top K Frequent Elements
// Link: https://leetcode.com/problems/top-k-frequent-elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #use min heap to find most freq ones( max frequency)
        heap=[]
        freq=Counter(nums) # m elements -> m==number of unique elements
        for num,count in freq.items():
            heapq.heappush(heap,(count,num))
            if len(heap)>k:
                heapq.heappop(heap)
        return [num for count,num in heap]

        