def sort_stack(arr):
  stack = []
  N = len(arr)
  
  while len(stack) <= N and arr:
    a = arr.pop()
    b = float('-inf') if len(stack) == 0 else stack.pop()
    while len(stack) and b > a:
      arr.append(b)
      b = stack.pop()
    
    stack.append(b)
    stack.append(a)
  
  return stack[1:]



def sortStack(arr):
  if len(arr) == 0:
    return arr
  
  top = arr.pop()
  
  sortStack(arr)

  insertInOrder(arr, top)
  
  return arr

def insertInOrder(stack, value):
  if len(stack) == 0 or stack[len(stack) - 1] <= value:
    stack.append(value)
    return

  top = stack.pop()
  
  insertInOrder(stack, value)
  
  print(top)
  stack.append(top)
  
  

arr = [-5, 2, -2, 4, 3, 1]
# result = sort_stack(arr)

# print(result)
print(sortStack(arr))