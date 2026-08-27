// Pattern: speed and time confusion can occur. Be careful
// Difficulty: Medium
// Problem: 875. Koko Eating Bananas
// Link: https://leetcode.com/problems/koko-eating-bananas

class Solution:
    def find_hours(self,piles,speed):
        hrs=0
        for pile in piles:
            hrs+=ceil(pile/speed)
        return hrs
            


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k is the speed
        low=1 #minimum speed is 1 banana per hour to finish in sum(piles) number of hours
        ans=max(piles)
        high=max(piles) # highest speed will be eating the max(piles) per hour to finish in n number of hours
        while(low<=high):
            mid=(low+high)//2
            hours= self.find_hours(piles,mid)
            # if hours==h:
            #     return mid ---> there might be even smaller speed that gives the same h so we see
            if hours<=h:
                ans=min(ans,mid)
                high=mid-1
            else:
                low=mid+1
        return ans


        