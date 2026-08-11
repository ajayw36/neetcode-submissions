# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, start, end):
        prev, curr = None, start
        while True:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            if prev == end: break
        return end, start

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = dummy
        while curr:
            start = curr.next
            for i in range(k):
                if not curr:
                    break
                curr = curr.next
            if not curr: break

            end = curr
            post = curr.next

            start, end = self.reverse(start, end)

            prev.next = start
            end.next = post

            curr = end
            prev = end

        return dummy.next


            
