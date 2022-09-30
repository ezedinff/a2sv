# [Stack](./stack.py) (LIFO)
- the newest element added to the queue will be processed first.
## Applications
- undo/redo
- back button in browser
- call stack

## [Min Stack](min-stack.py)
- keep track of the minimum element in the stack

## Questions
1. [Valid Parentheses](valid-parentheses.py)
- technique: stack
- when we see an opening bracket, we push it onto the stack
- when we see a closing bracket, we pop the stack and check if the popped element is a matching opening bracket
- if it is, we continue
- if it is not, we return false
- if the stack is empty at the end, we return true

2. [Evaluate Reverse Polish Notation](evaluate-reverse-polish-notation.py)
- technique: stack
- if the token is a number, push it onto the stack
- if the token is an operator, pop the top two elements from the stack, perform the operation, and push the result back onto the stack
- at the end, the stack will contain the result

3. [Daily Temperatures](daily-temperatures.py)
- technique: stack
- we iterate through the array from right to left
- we keep a stack of indices of temperatures that have not found a warmer temperature yet
- if the current temperature is warmer than the top of the stack, we pop the stack
- we keep popping until the stack is empty or the current temperature is not warmer than the top of the stack
- we then push the current index onto the stack
- we then set the result at the current index to be the difference between the current index and the top of the stack

## Stack and DFS
- we can use a stack to perform DFS, DFS is a recursive algorithm that uses a stack to keep track of the nodes to visit, DFS can be used to find the path from the root node to the target node
- procedure:
    1. push the root node onto the stack
    2. while the stack is not empty:
        1. pop the top node from the stack
        2. if the node is the target node, return the path
        3. push the children of the node onto the stack

```python
def dfs(root, target, visited) -> boolean:
    stack = [root]
    while stack:
        node = stack.pop()
        if node == target:
            return True
        for child in node.children:
            if child not in visited:
                stack.append(child)
                visited.add(child)
    return False
```




