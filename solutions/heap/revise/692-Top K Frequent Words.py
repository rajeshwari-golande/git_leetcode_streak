// Pattern: lexiographic proper order (ascending of count along with the wor lexio)
// Difficulty: Medium
// Problem: 692. Top K Frequent Words
// Link: https://leetcode.com/problems/top-k-frequent-words

class Word:
    def __init__(self,word):
        self.word=word
    def __lt__(self,other):
        return self.word>other.word


class Solution:

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap=[]
        freq=Counter(words)
        for word,count in freq.items():
            heapq.heappush(heap,(count,Word(word)))
            if len(heap)>k:
                heapq.heappop(heap)
        ans=[item[1].word for item in heap]
        return sorted(ans,key=lambda word: (-freq[word] , word))  
        