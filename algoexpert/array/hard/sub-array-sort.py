def sub_array_sort(array):
  min_val = float('inf')
  max_val = float('-inf')
  
  for i in range(len(arr)):
    num = array[i]
    if is_out_of_order(i, num, array):
      min_val = min(min_val, num)
      max_val = max(max_val, num)
  
  if min_val == float('inf'):
    return [-1, -1]
    
  ans = [-1, -1]
  
  i, j = 0, len(array) - 1
  while i < j:
    if array[i] > min_val and ans[0] == -1:
      ans[0] = i
    
    if array[j] < max_val and ans[1] == -1:
      ans[1] = j
  
    if ans[0] != -1 and ans[1] != -1:
      break
  
    i += 1
    j -= 1
  
  return ans


def is_out_of_order(index, num, array):
  if index == 0:
    return num > array[index + 1]
    
  if index == len(array) - 1:
    return num < array[index - 1]

  return array[index - 1] > num or num > array[index + 1]

  
arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

print(sub_array_sort(arr))
