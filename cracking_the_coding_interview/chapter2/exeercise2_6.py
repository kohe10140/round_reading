from LinkedList import LinkedList, LinkedListNode

def palindorme(linked_list: LinkedList) -> bool:
    node = linked_list.head
    inv_node = LinkedListNode(node.value)
    while node:
        node = node.next
        if node is not None:
            inv_node = LinkedListNode(node.value, nextNode=inv_node)

    node = linked_list.head
    while node:
        if node.value != inv_node.value:
            return False
        else:
            node = node.next
            inv_node = inv_node.next
    return True
    

a = LinkedList([3, 5, 8, 5, 10, 2, 1])
print(a)
print(palindorme(a))
print('')    
        
a = LinkedList([3, 5, 8, 5, 8, 5, 3])
print(a)
print(palindorme(a))
print('')    

a = LinkedList([1, 2, 3, 3, 2, 1])
print(a)
print(palindorme(a))
print('')    

a = LinkedList([3])
print(a)
print(palindorme(a))
print('')    