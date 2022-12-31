# node depth
class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right
  

def from_list(elements):
    root_node = TreeNode(x=elements[0])
    nodes = [root_node]
    for i, x in enumerate(elements[1:]):
        if x is None:
            continue
        parent_node = nodes[i // 2]
        is_left = (i % 2 == 0)
        node = TreeNode(x=x)
        if is_left:
            parent_node.left = node
        else:
            parent_node.right = node
        nodes.append(node)

    return root_node


def print_recursive(tree, level=0, prefix="root"):
    print(level * '  ' + prefix + " :" + "val=" + str(tree.val))
    if tree.left:
        print_recursive(tree.left, level + 1, "left")
    if tree.right:
        print_recursive(tree.right, level + 1, "right")
      
      
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
root = from_list(arr)

# print_recursive(root)

def node_depth(root, d = 0):
  if root is None:
    return 0
  return d + node_depth(root.left, d + 1) + node_depth(root.right, d + 1)
  


print(node_depth(root))