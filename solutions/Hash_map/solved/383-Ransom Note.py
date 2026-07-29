// Pattern: CHANGE_ME
// Difficulty: Easy
// Problem: 383. Ransom Note
// Link: https://leetcode.com/problems/ransom-note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        maga = {}

        for ch in magazine:
            maga[ch] = maga.get(ch, 0) + 1

        for ch in ransomNote:
            if maga.get(ch, 0) == 0:
                return False
            maga[ch] -= 1

        return True