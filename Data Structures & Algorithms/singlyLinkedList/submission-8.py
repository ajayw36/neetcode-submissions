class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        curr = self.head
        for i in range(index):

            if curr == None:
                return -1
            curr = curr.next
        return curr.val if curr else -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val, self.head)
        self.head = new_node
        if not self.tail: self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val, None)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head: self.head = new_node

    def remove(self, index: int) -> bool:
        if index == 0:
            if self.head:
                self.head = self.head.next
                if not self.head:
                    self.tail = None
                return True
            return False
        
        curr, prev = self.head, None
        for i in range(index):
            if not curr:
                return False
            prev = curr
            curr = curr.next
        if not curr:
            return False
        
        prev.next = curr.next
        if not prev.next:
            self.tail = prev

        return True

    def getValues(self) -> List[int]:
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

