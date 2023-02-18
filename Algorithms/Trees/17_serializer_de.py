import pickle
import sys

from Algorithms.Trees.base import create_bst, display_level_order, BinaryTreeNode

MARKER = sys.maxsize


def serialize(node, stream):
    if not node:
        stream.dump(MARKER)
        return
    stream.dump(node.data)
    serialize(node.left, stream)
    serialize(node.right, stream)


def deserialize(stream):
    try:
        data = pickle.load(stream)
        if data == MARKER:
            return None

        node = BinaryTreeNode(data)
        node.left = deserialize(stream)
        node.right = deserialize(stream)
        return node
    except pickle.UnpicklingError:
        return None


arr = [100, 50, 200, 25, 75, 125, 350]
root = create_bst(arr)
display_level_order(root)
output = open('data.tmp', 'wb')
p = pickle.Pickler(output)
serialize(root, p)
output.close()
input2 = open('data.tmp', 'rb')
root_deserialized = deserialize(input2)
print("Result:")
display_level_order(root_deserialized)