from typing import Iterable
from collections import deque

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f"Node: {self.data}"

    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    @staticmethod
    def insert_after(prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def __init__(self, nodes: Iterable[int] = None):
        self.head = None
        if nodes:
            self.insert_from(nodes)

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_from(self, nodes: Iterable[int]):
        for node in nodes:
            self.insert_at_end(node)

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev

    def get_node_list(self):
        lst = []
        current = self.head
        while current:
            lst.append(current)
            current = current.next
        return lst

    def sort(self, reverse=False):
        node_list = self.get_node_list()
        node_list.sort(key=lambda x: x.data, reverse=reverse)
        node_list = deque(node_list)
        self.head = node_list.popleft()
        current = self.head
        while node_list:
            current.next = node_list.popleft()
            current = current.next
        current.next = None

    def merge_sorted_lists(self, other_list: "LinkedList"):
        if not self.head:
            self.head = other_list.head
            return
        if not other_list.head:
            return

        list_1 = deque(self.get_node_list())
        list_2 = deque(other_list.get_node_list())
        node_1 = list_1.popleft()
        node_2 = list_2.popleft()

        self.head = None
        prev = None
        while node_1 or node_2:
            if not node_2 or (node_1 and node_1.data <= node_2.data):
                current = node_1
                node_1 = list_1.popleft() if list_1 else None
            else:
                current = node_2
                node_2 = list_2.popleft() if list_2 else None
            if not self.head:
                self.head = current
            if not prev:
                prev = current
            prev.next = current
            prev = current

    def __str__(self):
        return f"LinkedList: {str([x.data for x in self.get_node_list()])}"