arr = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

def binarySearch(arr, target):
  mid = len(arr) // 2
  while mid >= 0 and len(arr):
    if arr[mid] < target:
      arr = arr[:mid]
    elif arr[mid] > target:
      arr = arr[mid + 1:]
    else:
      return True
      
    mid = len(arr) // 2
    
  
  return False
  

print(binarySearch(arr, 9))




def binarySearch2(arr, target):
  start = 0
  end = len(arr) - 1
  while start < end :
    mid = (start + end) // 2
    if arr[mid] < target :
      start = mid +1
    elif arr[mid] > target:
      end = mid - 1
    else:
      return mid
  return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8]

print(binarySearch2(arr, 7))


def recursive_binary_search(arr, target):
  if len(arr) == 0:
    return False

  mid = len(arr) // 2
  if arr[mid] == target:
    return True
  elif arr[mid] > target:
    return recursive_binary_search(arr[:mid], target)
  else:
    return recursive_binary_search(arr[mid + 1:], target)


print(recursive_binary_search(arr, 0))



def re_binary_search(arr, target):
  return re_binary_search_helper(arr, target, 0, len(arr) - 1)

def re_binary_search_helper(arr, target, start, end):
  if start > end:
    return -1
  
  mid = (start + end) // 2
  if arr[mid] > target:
    return re_binary_search_helper(arr, target, start, mid - 1)
  elif arr[mid] < target:
    return re_binary_search_helper(arr, target, mid + 1, end)
  else:
    return mid