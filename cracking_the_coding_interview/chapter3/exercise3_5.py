from Stack import Stack

def sort_stack(s: Stack) -> Stack:
    sorted_stack = Stack()
    sorted_stack.push(s.pop())
    while not s.is_empty():
        temp = s.pop()
        while not sorted_stack.is_empty():
            if sorted_stack.peek() <= temp:
                sorted_stack.push(temp)
                break
            else:
                s.push(sorted_stack.pop())
    
    return sorted_stack

s = Stack([2, 5, 1, 3, 0])
print(s)
print(sort_stack(s))
print('')

s = Stack([2, 2, 2, 3, 2])
print(s)
print(sort_stack(s))
print('')