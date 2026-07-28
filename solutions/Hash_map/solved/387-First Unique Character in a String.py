// Pattern: dict / hash_map 
// Difficulty: Easy
// Problem: 387. First Unique Character in a String
// Link: https://leetcode.com/problems/first-unique-character-in-a-string

class Solution:
    def firstUniqChar(self, s: str) -> int:
        string_count={}
        for ch in s:
            string_count[ch]=string_count.get(ch,0)+1
        for i,ch in enumerate(s):
            if string_count[ch]==1:
                return i
        # for i in range(len(s)):
        #     if string_count[s[i]]==1:
        #         return i
        return -1

            
        