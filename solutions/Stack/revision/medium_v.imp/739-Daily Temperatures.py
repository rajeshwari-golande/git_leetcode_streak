// Pattern: stack pattern
// Difficulty: Medium
// Problem: 739. Daily Temperatures
// Link: https://leetcode.com/problems/daily-temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #next greater
        n=len(temperatures)
        warm_tempratures=[0]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while(stack and temperatures[stack[-1]]<=temperatures[i]):
                stack.pop()
            if not stack:
                warm_tempratures[i]=0
            else:
                warm_tempratures[i]=stack[-1]-i
            stack.append(i)
        return warm_tempratures