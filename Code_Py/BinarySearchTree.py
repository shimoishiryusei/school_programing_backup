import timeit
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        left = f'[{self.left.value}]' if self.left else '[]'
        right = f'[{self.right.value}]' if self.right else '[]'
        return f'{left} <- {self.value} -> {right}'

class BinarySearchTree:
    def __init__(self):
        self.nodes = []

    def add_node(self, value):
        node = Node(value)
        if self.nodes:
            parent, direction = self.find_parent(value)
            if direction == 'left':
                parent.left = node
            else:
                parent.right = node

        self.nodes.append(node)

    def find_parent(self, value):
        node = self.nodes[0]
        while node:
            p = node
            if p.value == value:
                raise ValueError('すでにある値と同じ値を格納することはできません．')
            if p.value > value:
                direction = 'left'
                node = p.left
            else:
                direction = 'right'
                node = p.right
        return p, direction

def main(li):
    btree=BinarySearchTree()
    for v in li:
        btree.add_node(v)

    for node in btree.nodes:
        print(node)

n_len = int(input("配列の要素数："))
li = [int(input()) for _ in range(n_len)]

main(li)
print(timeit.timeit('main',globals=globals(),number=1))