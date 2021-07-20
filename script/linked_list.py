# -*- coding: utf-8 -*-

# 判断一个链表是否有环，尾节点node.next == self._head成立即可!
class SingleNode(object):
    """单链表的结点"""
    def __init__(self,item):
        # _item存放数据元素
        self.item = item
        # _next是下一个节点的标识
        self.next = None

class SingleLinkList():
    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None

    def length(self):
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            # print(head.item)
            # 将cur后移一个节点
            head = cur.next
        return count

    def append(self, value):
        cur = self._head
        while cur != None:
            # print(head.item)
            # 将cur后移一个节点
            if cur.next == None:
                end_value = SingleNode(value)
                cur.next = end_value
                break
            head = cur.next

    def add(self, value):
        cur = self._head
        node = SingleNode(value)
        node.next = cur
        self._head = node

    def travel(self):
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next

    def insert(self, pos, value):
        cur = self._head
        if pos <= 0:
            self.add(value)
        elif pos > (self.length() - 1):
            self.append(value)
        else:
            node = SingleNode(value)
            count = 0
            pre = cur
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node

    def remove(self, value):
        cur = self._head
        pre = None
        while cur != None:
            if cur.item == value:
                if not pre:
                    self._head = cur.next
                else:
                    pre.next = cur.next
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

def test(head):
    head.next = SingleNode(2)
    head = head.next
    head.next = SingleNode(3)

if __name__ == "__main__":
    # ll = SingleLinkList()
    # ll.add(1)
    # ll.add(2)
    # IsFound = ll.search(2)
    # ll.travel()
    # print(IsFound)
    # IsEmpty = ll.is_empty()
    # print(IsEmpty)

    head = SingleNode(1)
    print(head)
    test(head)
    print(head.next.next.item)



