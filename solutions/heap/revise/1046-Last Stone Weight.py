// Pattern: easy greedy  pattern
// Difficulty: Easy
// Problem: 1046. Last Stone Weight
// Link: https://leetcode.com/problems/last-stone-weight

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we need to find the 2 max elements in the present array for evvery instant --> max heap
        heap=[]
        for stone in stones:
            heapq.heappush(heap,-stone)
        # n=len(stones)
        while(1):
            if not heap:
                return 0
            if len(heap)==1:
                return -heapq.heappop(heap)
            first_largest= -heapq.heappop(heap)
            second_largest=-heapq.heappop(heap)
            if first_largest!=second_largest:
                heapq.heappush(heap,-(first_largest-second_largest))

# Time: O(n log n)
# Space: O(n)

        