// Pattern: dictionary
// Difficulty: Easy
// Problem: 1189. Maximum Number of Balloons
// Link: https://leetcode.com/problems/maximum-number-of-balloons

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count_balloons={'b':0,'a':0,'l':0,'o':0,'n':0}
        for ch in text:
            if ch in count_balloons:
                count_balloons[ch]+=1
        instance=float('inf')
        for ch,count in count_balloons.items():
            if ch in {'l','o'}:
                instance=min(instance,count_balloons[ch]//2)
            else:
                instance=min(instance,count_balloons[ch])
        return instance

