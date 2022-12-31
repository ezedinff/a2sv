def find_loop(head):
  start = head.next
  end = head.next.next
  
  while start != end:
    start = start.next
    end = end.next.next
    
  end = head
  
  while start != end:
    start = start.next
    end = end.next
  
  return start