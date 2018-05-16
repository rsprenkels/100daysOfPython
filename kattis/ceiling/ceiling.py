class Ceiling:

    def run(self):
        num_prototypes, num_layers = list(map(int, input().split()))
        tree_shapes = set()
        for proto in range (num_prototypes):
            tree = Tree()
            values = list(map(int, input().split()))
            for value in values:
                tree.insert(value)
            tree_shapes.add(tree.getShape())
        print(len(tree_shapes))

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def getShape(self):
        id = ''
        if self.value is not None:
            id = 'R'
        if self.left is not None:
            id += 'l' + self.left.getShape()
        if self.right is not None:
            id += 'r' + self.right.getShape()
        return id

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            search_node = self.root
            found = False
            while not found:
                if value < search_node.value and search_node.left is not None:
                    search_node = search_node.left
                elif value >= search_node.value and search_node.right is not None:
                    search_node = search_node.right
                else:
                    found = True
            if value < search_node.value:
                search_node.left = Node(value)
            else:
                search_node.right = Node(value)

    def getShape(self):
        if self.root is None:
            return ''
        else:
            return self.root.getShape()

if __name__ == '__main__':
    Ceiling().run()