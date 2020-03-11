class Node(object):
    """节点类"""

    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    """docstring for Tree"""

    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, elem):
        node = Node(elem)
        if self.root.elem == -1:
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)  # 如果该结点存在右子树，将此结点丢弃。

    '''
        ①、中序遍历:左子树——》根节点——》右子树

　　     ②、前序遍历:根节点——》左子树——》右子树

　　     ③、后序遍历:左子树——》右子树——》根节点
    '''

    def front_re(self, root):
        if root == None:
            return None
        print(root.elem)
        # 根节点——》左子树——》右子树
        self.front_re(root.lchild)
        self.front_re(root.rchild)

    def middle_re(self, root):
        if root == None:
            return None
        # 左子树——》根节点——》右子树
        self.middle_re(root.lchild)
        print(root.elem)
        self.middle_re(root.rchild)

    def later_re(self, root):
        if root == None:
            return None
        # 后序遍历:左子树——》右子树——》根节点
        self.later_re(root.lchild)
        self.later_re(root.rchild)
        print(root.elem)

    def level_queue(self, root):
        if root == None:
            return None
        myQueue = []
        node = root
        myQueue.append(node)

        while myQueue:
            node = myQueue.pop(0)
            print(node.elem)

            if node.lchild != None:
                myQueue.append(node.lchild)
            if node.rchild != None:
                myQueue.append(node.rchild)

    def front_stack(self, root):
        if root == None:
            return None
        myStack = []
        node = root
        # 从根节点开始，一直找它的左子树
        while node or myStack:
            while node:
                print(node.elem)
                myStack.append(node)
                node = node.lchild
            # while结束表示当前节点node为空，
            # 即前一个节点没有左子树了
            node = myStack.pop()
            node = node.rchild
            # 开始查看它的右子树

    def middle_stack(self, root):
        if root == None:
            return None
        myStack = []
        node = root

        while node or myStack:
            while node:
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()
            print(node.elem)
            node = node.rchild

    def later_stack(self, root):
        if root == None:
            return None
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)

        while myStack1:
            node = myStack1.pop()
            if node.lchild:
                myStack1.append(node.lchild)
            if node.rchild:
                myStack1.append(node.rchild)
            myStack2.append(node)

        while myStack2:
            print(myStack2.pop().elem)


# elems = ['A','B','C','D','E','F','G'\
#         ,'H','I','J','K','L','M','N','O']
elems = range(15)
tree = Tree()
for elem in elems:
    tree.add(elem)
'''
        0
       / \
      1   2
     / \ / \
    3  4 5  6
   / \      / \
'''

# tree.front_re(tree.root) #根-左-右
tree.later_stack(tree.root)  # 左-根-右
