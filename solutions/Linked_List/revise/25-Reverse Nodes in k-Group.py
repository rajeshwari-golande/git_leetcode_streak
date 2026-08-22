// Pattern : reverse every k element subarray
// Difficulty: Hard
// Problem: 25. Reverse Nodes in k-Group
// Link: https://leetcode.com/problems/reverse-nodes-in-k-group

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        group_prev=dummy
        group_start=head
        prev=head
        while True:
            node=group_start
            cnt=k
            while(node and cnt-1):
                cnt-=1
                node=node.next
            group_last=node
            if not group_last:
                break
            kth_node=group_last.next
            prev=kth_node
            root=group_start
            while(root and root!=kth_node):
                next_node=root.next
                root.next=prev
                prev=root
                root=next_node
            
            group_prev.next=group_last
            group_prev=group_start
            group_start=root

        return dummy.next

        