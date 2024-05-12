from Stack import Myqueue

myqueue = Myqueue()
print(f'Is initial state empty? -> {myqueue.is_empty()}')

for i in range(0, 20, 2):
    myqueue.add(i)
    print(f'peek is {myqueue.peek()}')

for i in range(0, 20, 2):
    rmv = myqueue.remove()
    print(f'deque {rmv}')
    print(f'peek is {myqueue.peek()}')

print(f'Is final state empty? -> {myqueue.is_empty()}')