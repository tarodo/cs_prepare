class MyLinkedList:

    def __init__(self):
        self.val = -1
        self.next_el = None

    def get(self, index: int) -> int:
        el = self
        for idx in range(index):
            if el.next_el:
                el = el.next_el
            else:
                return -1
        return el.val

    def addAtHead(self, val: int) -> None:
        if self.val == -1:
            self.val = val
            return
        new_el = MyLinkedList()
        new_el.val = self.val
        new_el.next_el = self.next_el
        self.val = val
        self.next_el = new_el

    def addAtTail(self, val: int) -> None:
        if self.val == -1:
            self.val = val
            return

        el = self
        while el.next_el:
            el = el.next_el
        new_el = MyLinkedList()
        new_el.val = val
        el.next_el = new_el

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        cur_el = self
        for idx in range(1, index):
            if cur_el.next_el:
                cur_el = cur_el.next_el
            else:
                return
        next_el = cur_el.next_el
        new_el = MyLinkedList()
        new_el.val = val
        new_el.next_el = next_el
        cur_el.next_el = new_el


    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.next_el:
                self.val = self.next_el.val
                self.next_el = self.next_el.next_el
            else:
                self.val = -1
            return
        cur_el = self
        for idx in range(1, index):
            if cur_el.next_el:
                cur_el = cur_el.next_el
            else:
                return
        if cur_el.next_el:
            cur_el.next_el = cur_el.next_el.next_el


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)