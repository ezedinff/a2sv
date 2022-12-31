# def pre_order(root):
#   if root is None:
#     return
#   print(root.val)
#   pre_order(root.left)
#   pre_order(root.right)


# def in_order(root):
#   if root is None:
#     return
#   in_order(root.left)
#   print(root.val)
#   in_order(root.right)


# def post_order(root):
#   if root is None:
#     return 
#   post_order(root.left)
#   post_order(root.right)
#   print(root.val)
  

# post_order(root)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
root = from_list(arr)

# print_recursive(root)

def branch_sum(root):
  result = []
  branch_sum_helper(root, 0, result)
  print(result)

def branch_sum_helper(root, sum, result):
  if root is None:
    return
  
  sum += root.val
  if root.left is None and root.right is None:
    result.append(sum)

  branch_sum_helper(root.left, sum, result)
  branch_sum_helper(root.right, sum, result)