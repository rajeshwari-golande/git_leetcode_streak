// Pattern: good usage of demorgen's law in the proper format for the intersection
// Difficulty: Medium
// Problem: 986. Interval List Intersections
// Link: https://leetcode.com/problems/interval-list-intersections

# Non-overlap: (A.end < B.start) OR (A.start > B.end)
# Overlap = NOT(Non-overlap) = NOT(A.end < B.start) AND NOT(A.start > B.end) = (A.end >= B.start) AND (A.start <= B.end)


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n1=len(firstList)
        n2=len(secondList)
        i=0
        j=0
        merged=[]
        intersect=[]
        while(i<n1 and j<n2):
            if firstList[i][0]<=secondList[j][1] and firstList[i][1]>=secondList[j][0]:#overlapping condition
                merged.append([max(firstList[i][0],secondList[j][0]),min(firstList[i][1],secondList[j][1])])
                if firstList[i][1]<secondList[j][1]:
                    i+=1
                elif firstList[i][1]>secondList[j][1]:
                    j+=1
                else:
                    i+=1
                    j+=1
            else:
                if firstList[i][1]<secondList[j][1]:
                    i+=1
                else:
                    j+=1
        return merged
                

        