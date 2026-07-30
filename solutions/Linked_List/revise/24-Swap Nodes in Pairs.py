// Pattern: ll reversal pattern
// Difficulty: Medium
// Problem: 24. Swap Nodes in Pairs
// Link: https://leetcode.com/problems/swap-nodes-in-pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        curr=head
        prev=ListNode()
        while(curr and curr.next):
            print(curr.val)
            next_node=curr.next
            if curr==head:
                head=next_node
            curr.next=next_node.next
            next_node.next=curr
            prev.next=next_node
            prev=curr
            curr=curr.next
        return head
        