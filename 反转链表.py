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

# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL


nodes = [1, 2, 3, 4, 5]
l1 = generateLinkedList(nodes)


def reverseList(head):

    if head == None or head.next == None:
        return head
    p = reverseList(head.next)
    head.next.next = head
    head.next = None

    return p


ans = reverseList(l1)

while ans:
    print(ans.val)
    ans = ans.next
