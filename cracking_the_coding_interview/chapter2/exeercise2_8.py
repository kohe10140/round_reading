from LinkedList import LinkedList, LinkedListNode

def get_loop_start(linked_list: LinkedList) -> LinkedListNode:
    node = linked_list.head
    cnt = 0
    while node:
        check = linked_list.head
        for _ in range(cnt):
            if node is check:
                #breakpoint()
                return check
            check = check.next
        cnt += 1
        node = node.next


def get_loop_start2(linked_list: LinkedList) -> LinkedListNode:
    fast = linked_list.head
    slow = linked_list.head
    fast = fast.next.next
    slow = slow.next
    while fast and slow:
        if fast is slow:
            slow = linked_list.head
            while fast and slow:
                if fast is slow:
                    return slow
                fast = fast.next
                slow = slow.next
        fast = fast.next.next
        slow = slow.next


a = LinkedList([0, 1, 2, 3, 4])
a.tail.next = a.head.next.next
print(get_loop_start(a))
print(get_loop_start2(a))
print('')      

a = LinkedList([0, 1, 2, 3, 4])
a.tail.next = a.head
print(get_loop_start(a))
print(get_loop_start2(a))
print('')      

a = LinkedList([0])
a.tail.next = a.head
print(get_loop_start(a))
print(get_loop_start2(a))
print('')    
