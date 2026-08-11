# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        left = dummy
        left.next = head
        right = head

        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            right = right.next
            left = left.next
        
        if left == dummy:
            return head.next

        left.next = left.next.next
        return head
        