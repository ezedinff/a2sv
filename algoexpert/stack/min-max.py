class MinMaxStack:
  def __init__(self):
    self.items = [] # stack
    self.min_max_stack = []
    # {min: number, max: number}
  
  
  def push(self, item):
    min_max = { "min": item, "max": item } # default
    
    if not self.is_empty():
      last_min_max = self.min_max_stack[-1]
      min_max["min"] = min(last_min_max["min"], item)
      min_max['max'] = max(last_min_max['max'], item)
    
    self.min_max_stack.append(min_max)
    self.items.append(item)
  
  
  def pop(self):
    self.min_max_stack.pop()
    return self.items.pop()
  
  
  def peek(self):
    return self.items[-1]
  
  def size(self):
    return len(self.items)
  
  def is_empty(self):
    return self.size() == 0
    
  def getMax(self):
    return self.min_max_stack[-1]['max']

  def getMin(self):
    return self.min_max_stack[-1]['min']




stack = MinMaxStack()
stack.push(5)
stack.push(7)
stack.push(2)
print("min =>", stack.getMin())
print("max =>", stack.getMax())
print("peek =>", stack.peek())  