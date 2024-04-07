from LinkedList import LinkedList

def partition(linked_list: LinkedList, x:int) -> LinkedList:
    node = linked_list.head
    lower = LinkedList()
    upper = LinkedList()
    while node is not None:
        if node.value < x:
            lower.add(node.value)
        else:
            upper.add(node.value)
        node = node.next
    lower.tail.next = upper.head
    return lower
    

a = LinkedList([3, 5, 8, 5, 10, 2, 1])
print(a)
print(partition(a, 5))
        