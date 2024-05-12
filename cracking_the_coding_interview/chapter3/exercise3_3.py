from Stack import SetOfStacks

sos = SetOfStacks(max_size=3)

for i in range(10):
    sos.push(i)
    print(f'push {i}')
    print(f'Top of stack set {sos.stack_set.top.value.top.value}')
    print(f'size Top of stack set {sos.stack_set.top.value.size}')
    print(f'size of stack set {sos.stack_set.size}')
    print('')

for i in range(10):
    popped = sos.pop()
    print(f'popped {popped}')
    if sos.stack_set.top:
        print(f'Top of stack set {sos.stack_set.top.value.top.value}')
        print(f'size Top of stack set {sos.stack_set.top.value.size}')
    print(f'size of stack set {sos.stack_set.size}')
    print('')