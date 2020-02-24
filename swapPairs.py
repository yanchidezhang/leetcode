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


n1 = [1,2,3,4,5,6,7,8]
l1 = generateLinkedList(n1)

# recursive method
def swapPairs(head):
    # return head if the input was empty or only contain 1 element
    if not head or not head.next: return head

    ptr1 = head
    ptr2 = head.next
    ptr3 = head.next.next

    # if we reach the bottom of the list
    if ptr2.next == None:
        # simply switch the pairs
        ptr2.next = ptr1
        ptr1.next = None
    # if we didn't reach the bottom
    else:
        # switch nodes
        ptr2.next = ptr1
        # call the swapPairs() function recursively
        # append the result to the current pairs
        ptr1.next = swapPairs(ptr3)

    return ptr2

ans = swapPairs(l1)

while ans:
    print(ans.val)
    ans = ans.next
