from LinkedList import LinkedList

def lsum(l1: LinkedList, l2: LinkedList) -> LinkedList:
    node1 = l1.head
    node2 = l2.head
    carry = 0
    while node1 or node2:
        if not node1:
            s = node2.value + carry
            l1.add(s%10)
            node2 = node2.next
            carry = int(s/10)
        elif not node2:
            s = node1.value + carry
            node1.value = s % 10
            node1 = node1.next
            carry = int(s/10)
        else:
            s = node1.value + node2.value + carry
            node1.value = s % 10
            carry = int(s/10)
            node1 = node1.next
            node2 = node2.next
    if carry == 1:
        l1.add(1)
    return l1
    

a = LinkedList([7, 1, 6])
b = LinkedList([5, 9, 2])
print('a     is ', a)
print('b     is ', b)
c = lsum(a, b)
print('a + b is ', c)
print('')
        
a = LinkedList([7, 1, 6])
b = LinkedList([5, 9, 3])
print('a     is ', a)
print('b     is ', b)
c = lsum(a, b)
print('a + b is ', c)
print('')

a = LinkedList([7, 1])
b = LinkedList([5, 9, 3])
print('a     is ', a)
print('b     is ', b)
c = lsum(a, b)
print('a + b is ', c)
print('')

a = LinkedList([7, 1, 6])
b = LinkedList([5, 9])
print('a     is ', a)
print('b     is ', b)
c = lsum(a, b)
print('a + b is ', c)
print('')

a = LinkedList([9, 9, 9])
b = LinkedList([1])
print('a     is ', a)
print('b     is ', b)
c = lsum(a, b)
print('a + b is ', c)
print('')