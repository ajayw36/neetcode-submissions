# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = False
        while l1 and l2:
            sum = l1.val + l2.val
            if carry: sum += 1
            carry = False
            if sum >= 10:
                sum = sum % 10
                carry = True
            
            curr.next = ListNode(sum)
            curr = curr.next

            l1 = l1.next
            l2 = l2.next
        
        while l1:
            sum = l1.val
            if carry: sum += 1
            carry = False
            if sum >= 10:
                sum = sum % 10
                carry = True
            curr.next = ListNode(sum)
            curr = curr.next
            l1 = l1.next

        while l2:
            sum = l2.val
            if carry: sum += 1
            carry = False
            if sum >= 10:
                sum = sum % 10 
                carry = True
            curr.next = ListNode(sum)
            curr = curr.next
            l2 = l2.next
        
        if carry:
            curr.next = ListNode(1)
        
        return dummy.next