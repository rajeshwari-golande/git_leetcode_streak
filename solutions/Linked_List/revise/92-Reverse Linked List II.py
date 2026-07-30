// Pattern: interesting revelsal --> dummy->head is imp 
// Difficulty: Medium
// Problem: 92. Reverse Linked List II
// Link: https://leetcode.com/problems/reverse-linked-list-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        new_node=ListNode()
        dummy=ListNode()
        dummy.next=head
        left_prev_node=dummy
        right_prev_node=dummy
        l=0
        r=0
        if(head==None or head.next ==None):
            return head
        while( r<right-1):
            if l<left-1:
                left_prev_node=left_prev_node.next
            if r<right-1:
                right_prev_node=right_prev_node.next
            l+=1
            r+=1
        left_node=left_prev_node.next
        right_node=right_prev_node.next
        right_next_node=right_node.next
        prev_curr_node=left_prev_node
        curr_node=left_node
        for i in range(right-left+1):
            next_node=curr_node.next
            curr_node.next=prev_curr_node
            prev_curr_node=curr_node
            curr_node=next_node
        left_prev_node.next=right_node
        left_node.next=right_next_node
        return dummy.next




        


            
        