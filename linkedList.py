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


n1 = [1, 2, 4]
n2 = [1, 3, 4]

l1 = generateLinkedList(n1)
l2 = generateLinkedList(n2)

ptr1 = l1
ptr2 = l2
