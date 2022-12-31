def buildingsCanSeeSunSet(buildings, direction):
  d = range(0, len(buildings), 1) if direction == "EAST" else range(len(buildings) - 1, -1, -1)
  stack = []
  for i in d:
    if len(stack) == 0 or buildings[stack[-1]] > buildings[i]:
      stack.append(i)
    else:
      stack.pop()
      while stack and buildings[stack[-1]] <= buildings[i]:
        stack.pop()
      stack.append(i)
      
  
  if direction == "WEST":
    return stack[::-1]
      
  return stack
    
buildings = [3, 5, 4, 4, 3, 1, 3, 2]
direction = "WEST"
    
    
result = buildingsCanSeeSunSet(buildings, direction)

print(result)