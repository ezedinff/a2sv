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



l1 = get_list([2, 6, 7, 8])
l2 = get_list([1, 3, 4, 5, 9, 10])



def merge_list(l1, l2):
  p1, p2 = l1, l2
  prev = None
  while p1 and p2:
    if p1.val < p2.val:
      prev = p1 # save reference of current p1 element
      p1 = p1.next # go to next p1 element
      
    else:
      if prev is not None:
        prev.next = p2
      prev = p2
      p2 = p2.next
      prev.next = p1
  
  if p1 is None:
    prev.next = p2
    
  return l1 if l1.val < l2.val else l2