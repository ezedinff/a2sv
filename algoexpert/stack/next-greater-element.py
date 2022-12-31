def next_greater_element(arr):
  ans = [-1] * len(arr)
  stack = [0]
  
  index = 1
  
  while index < len(arr):
    while len(stack) and arr[stack[-1]] < arr[index]:
      if stack[-1] == index:
        stack.pop()
      elif arr[stack[-1]] < arr[index]:        
        el_index = stack.pop()
        ans[el_index] = arr[index]

    if ans[index] == -1 and index not in stack:
        stack.append(index)
    
    index += 1
    if len(stack):
      if index == len(arr):
        index = 0
      elif stack[-1] == index:
        break
  
  return ans
    


nums =  [2, 5, -3, -4, 6, 2, 7]

print(next_greater_element(nums))