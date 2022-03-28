# class Node:
#     def __init__(self, data, next):
#         self.data = data
#         self.next = next
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None  # there is no head atm?
#
#     def add_at_front(self, data):  # to add elements at head of the node
#         self.head = Node(data, self.head)  # to make new head, it needs the node(data + prev head?)
#         # every self.head is a node instance with 'head' and 'next' properties 5{4{3{2{1{None}}}}}
#         # Node 5 has 5 as 'data' and Node 4 as 'next'... Node 4 has 4 as 'data' and Node 3 as 'next'
#
#     def add_at_end(self, data):  # to add data towards the tail
#         if not self.head:  # if there is a head (ie head is not None)
#             self.head = Node(data, None)  # new head is created that points to None?
#             return
#         curr = self.head  # this is the current head
#         while curr.next:
#             curr = curr.next  # updating the current head to the next one
#         curr.next = Node(data, None)  # the new current head points to null
#
#     def get_last_node(self):
#         n = self.head
#         while (n.next != None):  # while n is not the last head
#             n = n.next  # update n to the next head
#         return n.data
#
#     def print_list(self):
#         n = self.head
#         while n != None:
#             print(n.data, end=" => ")
#             n = n.next
#         print(
# class Graph:
#     def __init__(self, size):
#         self.adj = [[0] * size for i in range(size)]
#         self.size = size
#
#     def add_edge(self, orig, dest):
#         if orig > self.size or dest > self.size or orig < 0 or dest < 0:
#             print("Invalid Edge")
#         else:
#             self.adj[orig - 1][dest - 1] = 1
#             self.adj[dest - 1][orig - 1] = 1
#
#     def remove_edge(self, orig, dest):
#         if orig > self.size or dest > self.size or orig < 0 or dest < 0:
#             print("Invalid Edge")
#         else:
#             self.adj[orig - 1][dest - 1] = 0
#             self.adj[dest - 1][orig - 1] = 0
#
#     def display(self):
#         for row in self.adj:
#             print()
#             for val in row:
#                 print("{: 4".format(val), end="")
#

import numpy as np

c = np.array([[[[1,2,3],[4,5,6],[-1,-2,-3]],[[1,2,3],[4,5,6],[-1,-2,-3]]],[[[1,2,3],[4,5,6],[-1,-2,-3]],[[1,2,3],[4,5,6],[-1,-2,-3]]]])
print(np.random.randint(5, size=2))

