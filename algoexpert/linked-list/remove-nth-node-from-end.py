class Node:
  def __init__(self, val = None, next = None):
    self.val = val
    self.next = next


# def remove_nth_node_from_end(head, n):
#   length = 1
#   node = head 
#   while node.next:
#     length += 1
#     node = node.next
    
#   pos = length - n
  
#   p = 1
#   node = head
#   while p < pos and node.next:
#     p +=1
#     node = node.next
  
#   node.next = node.next.next



def remove_nth_node_from_end(head, n):
  start = head
  end = head
  diff = 0
  
  while diff < n:
    end = end.next
    diff += 1
  
  if end is None:
    head.val = head.next.val
    head.next = head.next.next
  else:
    while end.next is not None:
      start = start.next
      end = end.next
    
    start.next = start.next.next



arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nth = 4

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



remove_nth_node_from_end(n, 10)

no = n
while no.next:
  print(no.val)
  no = no.next
print(no.val)