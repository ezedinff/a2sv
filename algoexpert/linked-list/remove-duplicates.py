class LinkedNode:
  def __init__(self, val = None, next = None):
    self.val = val
    self.next = next


def remove_duplicates(head):
  while head.next:
    if head.val == head.next.val:
      head.next = head.next.next
    else:
      head = head.next

arr = [1, 1, 3, 4, 4, 4, 5, 6, 6]
head = None
for num in arr:
  if not head:
    head = LinkedNode(num)
    continue

  new_node = LinkedNode(num)
  
  # find the tail
  tail = head
  while tail.next:
    tail = tail.next
    
  # the tail is found, so update the tail's next 
  tail.next = new_node


def print_linked_list(head):
  p = head
  while p.next:
    print(p.val)
    p = p.next
  
  print(p.val)


remove_duplicates(head)

print_linked_list(head)