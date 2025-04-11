from model.pet import Pet

class Node:
    def __init__(self, pet: Pet):
        self.pet = pet
        self.left = None
        self.right = None

class ABB:
    def __init__(self):
        self.root = None

    def add(self, pet: Pet):
        def insert(node, pet):
            if node is None:
                return Node(pet)
            if pet.id < node.pet.id:
                node.left = insert(node.left, pet)
            else:
                node.right = insert(node.right, pet)
            return node

        self.root = insert(self.root, pet)

    def inorder(self):
        result = []

        def traverse(node):
            if node:
                traverse(node.left)
                result.append(node.pet)
                traverse(node.right)

        traverse(self.root)
        return result

    def preorder(self):
        result = []

        def traverse(node):
            if node:
                result.append(node.pet)
                traverse(node.left)
                traverse(node.right)

        traverse(self.root)
        return result

    def postorder(self):
        result = []

        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                result.append(node.pet)

        traverse(self.root)
        return result
