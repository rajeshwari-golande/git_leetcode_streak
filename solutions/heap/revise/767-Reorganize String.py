// Pattern: greedy heap pattern
// Difficulty: Medium
// Problem: 767. Reorganize String
// Link: https://leetcode.com/problems/reorganize-string

class Solution:
    def reorganizeString(self, s: str) -> str:
        # we will use the char that has max freq at that point --> max heap
        heap=[]
        freq=dict()
        prev=(0,'')
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        for ch,fq in freq.items():
            heapq.heappush(heap,(-fq,ch))
        ans=""
        n=len(s)
        for i in range(n):
            if not heap:
                return ""
            fq,ch=heapq.heappop(heap)
            ans+=ch
            if prev[0]<0:
                heapq.heappush(heap,prev)
            prev=(fq+1,ch)
            
        return ans


            

            
        