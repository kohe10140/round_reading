from Stack import StackWithMin

a = StackWithMin([i for i in range(10)])
print(a)
print('min is ', a.min())

a = StackWithMin()
a.push(3)
a.push(100)
a.push(-1)
print(a)
print('min is ', a.min())
a.pop()
print(a)
print('min is ', a.min())
a.push(-2)
a.push(2)
a.push(-2)
print(a)
print('min is ', a.min())
a.pop()
print(a)
print('min is ', a.min())
a.pop()
print(a)
print('min is ', a.min())
a.pop()
print(a)
print('min is ', a.min())