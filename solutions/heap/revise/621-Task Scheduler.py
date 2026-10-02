// Pattern: good brainstorm
// Difficulty: Medium
// Problem: 621. Task Scheduler
// Link: https://leetcode.com/problems/task-scheduler

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        heap=[]
        freq=dict()
        for task in tasks:
            freq[task]=freq.get(task,0)+1
        n1=len(freq)
        #max heap --> because we want to finish the tasks with max freq
        free={}
        for ch,fq in freq.items():
            heapq.heappush(heap,(-fq,ch))
            free[ch]=free.get(ch,0)+1
        seat=1
        while(heap):
            pulled=[]
            # (fq,ch)=heapq.heappop(heap)
            while(heap): #to check until you get one which we can place
                (fq,ch)=heapq.heappop(heap)
                if free[ch]<=seat:
    
                    free[ch]=seat+n+1
                    fq+=1
                    if fq<0:
                        heapq.heappush(heap,(fq,ch))
                    break
                else:
                     pulled.append((fq,ch)) # like a deque

            for fq,ch in pulled:
                heapq.heappush(heap,(fq,ch))
            seat+=1
        return seat-1






        