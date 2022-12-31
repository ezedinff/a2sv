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



l1 = get_list([0, 1, 2, 3, 4, 5])


def reverse(head):
  start = head
  
  while start.val <= start.next.val:
    end = start
    
    # this loop controls end
    while end.next is not None and end.val <= end.next.val:
      end = end.next
    
    start.val, end.val = end.val, start.val # swap
    

    start = start.next # move to next element

def reverse2(head):
    start = None
    end = head
    while end:
        temp = end.next
        end.next = start
        start = end
        end = temp

    return start

print_list(l1)
print("============================")
reverse(l1)
print_list(l1)

