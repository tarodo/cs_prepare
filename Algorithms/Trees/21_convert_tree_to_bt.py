from Algorithms.Trees.base import BinaryTreeNode, display_level_order


def convert_n_ary_to_binary(node):
    return convert_n_ary_to_binary_rec(node, 1)


def convert_n_ary_to_binary_rec(root, is_left):
    if not root:
        return

    bt_node = BinaryTreeNode(root.data)
    last_node = bt_node

    for child in root.children:
        if is_left:
            last_node.left = convert_n_ary_to_binary_rec(child, 0)
            last_node = last_node.left
        else:
            last_node.right = convert_n_ary_to_binary_rec(child, 1)
            last_node = last_node.right

    return bt_node


def convert_binary_to_n_ary(node):
    return convert_binary_to_n_ary_rec(node, 1)


def convert_binary_to_n_ary_rec(node, isLeft):
    if not node:
        return

    nnode = TreeNode(node.data)
    temp = node

    if isLeft == 1:
        while temp.left != None:
            child = convert_binary_to_n_ary_rec(temp.left, 0)
            nnode.children.append(child)
            temp = temp.left
    else:
        while temp.right != None:
            child = convert_binary_to_n_ary_rec(temp.right, 1)
            nnode.children.append(child)
            temp = temp.right

    return nnode


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node1.children.append(node2)
node1.children.append(node3)
node1.children.append(node4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node3.children.append(node5)
node3.children.append(node6)

print("Original n-ary tree")
node1.display_level_order()
bnode1 = convert_n_ary_to_binary(node1)
print("Converted binary tree")
display_level_order(bnode1)

tnode1 = convert_binary_to_n_ary(bnode1)
print("\nConverted n-ary tree")
tnode1.display_level_order()
