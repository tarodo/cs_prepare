from collections import deque

from Algorithms.Trees.base import BinaryTreeNode, create_bst


class InorderIterator:
    def __init__(self, root):
        self.q = deque()
        self.collect_queue(root)

    def collect_queue(self, root: BinaryTreeNode):
        tmp = root
        while tmp:
            self.q.append(tmp)
            tmp = tmp.left

    # hasNext - given name
    def hasNext(self):
        if self.q:
            return True

    # getNext - given name
    def getNext(self):
        el = self.q.pop()
        self.collect_queue(el.right)
        return el


def inorder_using_iterator(root):
    inorder_iter = InorderIterator(root)
    result = ""
    while inorder_iter.hasNext():
        ptr = inorder_iter.getNext()
        result += str(ptr.data) + " "
    return result


arr = [25, 125, 200, 300, 75, 50, 12, 35, 60, 75]
root = create_bst(arr)
print("Inorder Iterator = ", end="")
print(inorder_using_iterator(root))
