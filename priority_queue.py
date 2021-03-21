import math
import sys


class PriorityQueue:
    """
    Priority queue using a min heap (complete binary tree in which the value in each internal node is smaller than or
    equal to the values in the children of that node.
    """

    def __init__(self):
        self.size = 0
        self.array = []
        self.position = {}

    def empty(self):
        """
        Check if the priority queue is empty.
        :return: True if empty, False otherwise.
        """
        return self.size == 0

    def min_heapify(self, i):
        """
        Heapify the node at index.
        :param i: the index.
        """
        left_child = self.left(i)
        right_child = self.right(i)
        if left_child < self.size and self.array[left_child[0]] < self.array[i[0]]:
            smallest = left_child
        else:
            smallest = i
        if right_child < self.size and self.array[right_child[0]] < self.array[smallest[0]]:
            smallest = right_child
        if smallest != i:
            self.swap(i, smallest)
            self.min_heapify(smallest)

    def insert(self, tup):
        """
        Insert a node into the priority queue.
        """
        self.position[tup[1]] = self.size
        self.size += 1
        self.array.append((sys.maxsize, tup[1]))
        self.decrease_key((sys.maxsize, tup[1]), tup[0])

    def extract_min(self):
        """
        Removes and returns the min element at the top of the priority queue.
        """
        min_node = self.array[0][1]
        self.array[0] = self.array[self.size - 1]
        self.size -= 1
        self.min_heapify(1)
        del self.position[min_node]
        return min_node

    def left(self, i):
        """
        Get the index of the left child.
        """
        return 2 * i + 1

    def right(self, i):
        """
        Get the index of the right child.
        """
        return 2 * i + 2

    def parent(self, i):
        """
        Get the index of the parent.
        :param i: 
        :return: 
        """""
        return math.floor(i / 2)

    def swap(self, i, j):
        """
        Swaps elements at indices i and j.
        """
        self.position[self.array[i][1]] = j
        self.position[self.array[j][1]] = i
        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp

    def decrease_key(self, tup, distance):
        i = self.position[tup[1]]
        self.array[i] = (distance, tup[1])
        while i > 0 and self.array[self.parent(i)][0] > self.array[i][0]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
