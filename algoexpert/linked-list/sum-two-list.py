class Node:
  def __init__(self, val = None, next = None):
    self.val = val
    self.next = next


def get_list(arr):
  n = None # head
  t = None # tail
  for num in arr:
    nw = Node(num) # new node
    if not n:
      n = nw
      t = nw
    else:
      t.next = nw # current tail next = new node
      t = nw # update tail pointer
  return n


def print_list(head):
  no = head
  while no:
    print(no.val)
    no = no.next



l1 = get_list([2, 4, 7, 8])
l2 = get_list([9, 4, 5, 9])

  
def sum_of_list(l1, l2):
  first = l1
  second = l2
  
  n = None
  t = None
  
  curry = 0
  
  while first or second or curry:
    fv, sv = 0, 0
    if first:
      fv = first.val
      first = first.next
    
    if second:
      sv = second.val
      second = second.next

    s = fv + sv + curry
    curry = s // 10
    
    new_node = None
    
    new_node = Node(s % 10)
    
    if n is None:
      n = new_node
      t = new_node
    else:
      t.next = new_node
      t = new_node
      
  
  return n

print_list(sum_of_list(l1, l2))