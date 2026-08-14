// Pattern: CHANGE_ME
// Difficulty: Easy
// Problem: 3090. Maximum Length Substring With Two Occurrences
// Link: https://leetcode.com/problems/maximum-length-substring-with-two-occurrences

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_occurance=0
        max_ch={}
        max_len=0
        left=0
        right=0
        n=len(s)
        while right<n:
            ch=s[right]
            max_ch[ch]=max_ch.get(ch,0)+1
            max_len+=1
            while(max_ch[ch]>2):
                max_ch[s[left]]-=1
                max_len-=1
                left+=1
            right+=1
            max_occurance=max(max_occurance,max_len)
        return max_occurance


        