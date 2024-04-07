from LinkedList import LinkedList

def get_len(linked_list: LinkedList) -> int:
    res = 0
    node = linked_list.head
    while node is not None:
        res += 1
        node = node.next
    return res

def get_k_to_last(linked_list: LinkedList, k: int) -> int:
    n = get_len(linked_list)
    node = linked_list.head
    for i in range(n-k):
        node = node.next
    return node

# 解法見てから
def get_k_to_last2(linked_list: LinkedList, k: int) -> int:
    node1 = linked_list.head
    node2 = linked_list.head
    for i in range(k):
        node2 = node2.next
    while node2 is not None:
        node1 = node1.next
        node2 = node2.next
    return node1

a = LinkedList([2, 4, 6, 8, 10])
print(a)
print(get_k_to_last(a, 2))
print(get_k_to_last2(a, 2))