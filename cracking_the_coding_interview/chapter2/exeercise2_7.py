from LinkedList import LinkedList

def is_common(l1: LinkedList, l2: LinkedList) -> bool:
    node1 = l1.head
    while node1:
        node2 = l2.head
        while node2:
            if node1 is node2:
                return True
            node2 = node2.next
        node1 = node1.next
    return False


a = LinkedList([3, 5, 8, 5, 10, 2, 1])
b = LinkedList([3, 5, 8, 5, 10, 2, 1])
print(a)
print(b)        
print(is_common(a, b))

a = LinkedList([1, 2, 4, 8, 16])
b = LinkedList([3, 6, 9, 12, 15])
b.head.next.next = a.head.next.next
print(a)
print(b)        
print(is_common(a, b))