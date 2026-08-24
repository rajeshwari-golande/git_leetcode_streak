// Pattern: rotate it 
// Difficulty: Medium
// Problem: 61. Rotate List
// Link: https://leetcode.com/problems/rotate-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node=head
        n=0
        while(node):
            n+=1
            last_node=node
            node=node.next
        cnt=0
        k=k%n  
        if k==0:
            return head,last_node,last_node
        node=head
        while(cnt<n):
            if cnt==n-k-1:
                end_node=node
            if cnt==n-k:
                first_node=node
            cnt+=1
            node=node.next
        return first_node,last_node,end_node
            



    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        first_node,last_node,end_node=self.find(head,k)
        last_node.next=head
        head=first_node
        end_node.next=None
        return head
        