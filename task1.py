from task1_linked_list import LinkedList, Node

init_list = [1, 2, 3, 4, 5]

linkedList = LinkedList(init_list)
print("Origin list:          ", linkedList)

def add_to_list_recursively(linkedList: LinkedList, node: Node):
    if node.next:
        add_to_list_recursively(linkedList, node.next)
    linkedList.insert_at_end(node.data)

def revert_list_recursively(linkedList: LinkedList):
    new_list = LinkedList()
    first_node = linkedList.head

    add_to_list_recursively(new_list, first_node)
    return new_list

print("Reversed recursively: ", revert_list_recursively(linkedList))

def revert_list_iteratively(linkedList: LinkedList):
    new_list = LinkedList()
    data_list = []
    current = linkedList.head
    while current:
        data_list.append(current.data)
        current = current.next
    for data in data_list[::-1]:
        new_list.insert_at_end(data)
    return new_list

print("Reverted iteratively: ", revert_list_iteratively(linkedList))
linkedList.reverse()
print("Reversed by link swap:", linkedList)

linkedList = LinkedList([5, 1, 4, 2, 3])
linkedList.sort()
print("Sorted:               ", linkedList)

list_1 = LinkedList([1, 3, 4, 8, 9])
list_2 = LinkedList([2, 5, 6, 7, 10])
list_1.merge_sorted_lists(list_2)
print("Merged:               ", list_1)