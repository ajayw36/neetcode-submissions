# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Step 1: Get the midpoint
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Step 2: Split the lists
        curr, prev = slow.next, None
        slow.next = None

        # Step 3: Reverse the second half
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Step 4: Merge the two halfs together
        list1, list2 = head, prev
        while list2:
            temp1 = list1.next
            temp2 = list2.next

            list1.next = list2
            list1 = temp1

            list2.next = list1
            list2 = temp2
        

        
