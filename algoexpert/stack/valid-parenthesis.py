def is_balanced(brackets):
  openings = { '(': 1, '{': 2, '[': 3 }
  closings = { ')': -1, '}': -2, ']': -3 }
  stack = []
  
  for bracket in brackets:
    print(stack)
    if bracket in closings.keys():
      if len(stack) == 0:
        return False
      else:
        if closings[bracket] + openings[stack.pop()] != 0:
          return False
      
    elif bracket in openings.keys():
      stack.append(bracket)
  
  print(stack)
  return len(stack) == 0
  


b = "(([]()()){})"
print(is_balanced(b))