class StackNode:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node
    
    def __str__(self):
        return str(self.value)

class Stack:

    def __init__(self, values=None):
        self.top = None
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
    
    def pop(self):
        item = self.top
        self.top = self.top.next
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