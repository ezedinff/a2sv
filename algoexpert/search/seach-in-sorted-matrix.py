arr = [
  [1, 4, 7, 12, 15, 1000],
  [2, 5, 19, 31, 32, 1001],
  [3, 8, 24, 33, 35, 1002],
  [40, 41, 42, 44, 45, 1003],
  [99, 100, 103, 106, 128, 1004]
]

def search(arr, target):
  row = 0
  col = len(arr[0]) - 1
  
  while row < len(arr) and col >= 0:
    print("steps")
    if arr[row][col] == target:
      return [row, col]
    elif arr[row][col] > target:
      col -= 1
    else:
      row += 1

  return [-1, -1] # not found
  



print(search(arr, 44))