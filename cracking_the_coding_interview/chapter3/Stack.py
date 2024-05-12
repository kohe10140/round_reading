class StackNode:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node
    
    def __str__(self):
        return str(self.value)

class Stack:

    def __init__(self, values=None):
        self.top = None
        self.size = 0
        if values is not None:
            for v in values:
                self.push(v)
    
    def __str__(self):
        node = self.top
        l = []
        while node:
            l.append(str(node))
            node = node.next
        return ' -> '.join(l)

    def push(self, value):
        t = StackNode(value)
        if self.top is not None:
            t.next = self.top
        self.top = t
        self.size += 1
    
    def pop(self):
        item = self.top
        self.top = self.top.next
        self.size -= 1
        return item.value
    
    def peek(self):
        return self.top.value
    
    def is_empty(self):
        if self.top:
            return False
        else:
            return True
    

class StackWithMin(Stack):

    def __init__(self, values=None):
        self.min_stack = Stack(values)
        self.top = None
        if values is not None:
            for v in values:
                self.push(v)
    
    def push(self, value):
        if self.min_stack.is_empty(): # if self.min_stack.is empty, self.min_stack.peek() raise an error
            self.min_stack.push(value)
        elif value <= self.min_stack.peek():
            self.min_stack.push(value)
        super().push(value)
    
    def pop(self):
        if self.min_stack.peek() == self.peek():
            self.min_stack.pop()
        super().pop()

    def min(self):
        return self.min_stack.peek()


class SetOfStacks:

    def __init__(self, max_size=100, values=None):
        self.stack_set = Stack() # type of self.stack_set is stack
        self.stack_set.push(Stack())
        self.max_size = max_size

        if values is not None:
            for v in values:
                self.push(v)

    def push(self, value):
        if self.stack_set.top.value.size >= self.max_size:
            self.stack_set.push(Stack())
        self.stack_set.top.value.push(value)

    def pop(self):
        popped_value = self.stack_set.top.value.pop()
        if self.stack_set.top.value.size == 0:
            self.stack_set.pop()
        return popped_value

    def popAt(self, index):
        # the index of top is 0
        stack = self.stack_set.top
        for i in range(index):
            stack = stack.next
        return stack.value.pop()


class Myqueue:

    def __init__(self, values=None):
        self.stack = Stack()

    def add(self, value):
        self.stack.push(value)

    def remove(self):
        self.inv_stack = Stack()
        while self.stack.top is not None:
            value = self.stack.pop()
            self.inv_stack.push(value)
        head = self.inv_stack.pop()
        while self.inv_stack.top is not None:
            value = self.inv_stack.pop()
            self.stack.push(value)
        return head

    def peek(self):
        if self.is_empty():
            return None
        stack_node = self.stack.top
        while stack_node.next is not None:
            stack_node = stack_node.next
        return stack_node.value

    def is_empty(self):
        return self.stack.is_empty()