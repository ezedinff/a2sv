def main():
    # Read number of queries
    num_queries = int(input())

    # Initialize variables
    ans = 0
    stack = [1]
    MAX = 2**32

    # Process queries
    for i in range(num_queries):
        query = input()

        # If query is "add", update answer and check for overflow
        if query == 'add':
            ans += stack[-1]
            if ans > MAX:
                print('OVERFLOW!!!')
                return

        # If query is "end", pop from stack
        elif query == 'end':
            stack.pop()

        # If query is "for", push new value to stack and check for overflow
        else:
            val = int(query[4:]) * stack[-1]
            stack.append(val)
            if val > MAX:
                print('OVERFLOW!!!')
                return

    # Print final answer
    print(ans)
