

class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.len = 0 
        

    def get(self, index: int) -> int:
        if index > self.len - 1 or index < 0:
            return -1
        cur = self.head
        idx = 0
        while idx < index:
            cur = cur.next
            idx += 1
        return cur.val

    def addAtHead(self, val: int) -> None:
        newhead = ListNode(val)
        newhead.next = self.head
        self.head = newhead
        self.len += 1

    def addAtTail(self, val: int) -> None:
        self.len += 1
        if not self.head:
            self.head = ListNode(val)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next  = ListNode(val)


    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.len:
            return
        
        self.len += 1
        if index == 0:
            newnode = ListNode(val)
            newnode.next = self.head
            self.head = newnode
            return
        
        cur = self.head
        idx = 0
        while idx < index:
            idx += 1
            pre = cur
            cur = cur.next
        newnode = ListNode(val)
        pre.next = newnode
        newnode.next = cur
        
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.len or index < 0:
            return
        self.len -= 1
        if index == 0:
            self.head = self.head.next
        cur = self.head
        idx = 0
        while idx < index:
            idx += 1
            pre = cur
            cur = cur.next
        pre.next = cur.next

        
if __name__ == '__main__':

    obj = MyLinkedList()  
    obj.addAtHead(1)
    obj.addAtTail(3)
    obj.addAtIndex(1,2)
    obj.get(1)
    obj.deleteAtIndex(0)
    obj.get(0)
