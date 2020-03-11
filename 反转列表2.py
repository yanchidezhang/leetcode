"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
"""

# LinkedList


class linkedNode():
    """docstring for linkedNode"""

    def __init__(self, val):
        self.val = val
        self.next = None


def generateLinkedList(nodes):
    head = linkedNode(nodes[0])
    ptr = head
    for i in range(1, len(nodes)):
        node = linkedNode(nodes[i])
        ptr.next = node

        ptr = ptr.next

    return head


nodes = [1, 2, 3, 4, 5]
l1 = generateLinkedList(nodes)
successor = None


class Solution():
    """docstring for Solution"""

    def __init__(self, head, m, n):
        self.successor = None
        self.head = head
        self.m = m
        self.n = n

    def returnBetween(self, head, m, n):
        if m == 1:
            return self.reverseN(head, n)

        head.next = self.returnBetween(head.next, m - 1, n - 1)

        return head

    def reverseN(self, head, N):
        if N == 1:
            self.successor = head.next
            return head

        last = self.reverseN(head.next, N - 1)
        head.next.next = head
        head.next = self.successor

        return last


rlt = Solution(l1, 2, 4)
nodes = rlt.returnBetween(l1, 3, 4)

while nodes:
    print(nodes.val)
    nodes = nodes.next
