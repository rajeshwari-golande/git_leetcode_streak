// Pattern: basic min heap
// Difficulty: Medium
// Problem: 215. Kth Largest Element in an Array
// Link: https://leetcode.com/problems/kth-largest-element-in-an-array

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #min-heap
        heap=[]
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]

# | Problem          | Heap used | Heap size |           Time |    Space |
# | ---------------- | --------- | --------: | -------------: | -------: |
# | **Kth Largest**  | Min heap  |       `k` | **O(n log k)** | **O(k)** |
