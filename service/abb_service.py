from model.abb import ABB
from model.pet import Pet

class ABBService:
    def __init__(self):
        self.tree = ABB()
        self.tree.add(Pet(id=10, name="Bobby", age=4, breed="golden retriever"))
        self.tree.add(Pet(id=3, name="Max", age=6, breed="bulldog"))

    def add_pet(self, pet: Pet):
        if self.check_pet_exists(pet.id):
            return {"error": "A pet with this ID already exists."}
        self.tree.add(pet)
        return {"message": "Pet added successfully"}

    def check_pet_exists(self, pet_id: int):
        current = self.tree.root
        while current is not None:
            if current.pet.id == pet_id:
                return True
            elif pet_id < current.pet.id:
                current = current.left
            else:
                current = current.right
        return False

    def count_breeds(self):
        breed_counts = {}

        def count(node):
            if node is not None:
                breed = node.pet.breed  # Asegúrate que sea .breed si tu clase Pet lo define así
                breed_counts[breed] = breed_counts.get(breed, 0) + 1
                count(node.left)
                count(node.right)

        count(self.tree.root)
        return breed_counts

    def remove_pet(self, pet_id: int):
        def delete(node, pet_id):
            if node is None:
                return None
            if pet_id < node.pet.id:
                node.left = delete(node.left, pet_id)
            elif pet_id > node.pet.id:
                node.right = delete(node.right, pet_id)
            else:
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                temp = find_min(node.right)
                node.pet = temp.pet
                node.right = delete(node.right, temp.pet.id)
            return node

        def find_min(node):
            while node.left is not None:
                node = node.left
            return node

        if not self.check_pet_exists(pet_id):
            return {"error": "Pet not found"}

        self.tree.root = delete(self.tree.root, pet_id)
        return {"message": "Pet removed successfully"}

    def update_pet_info(self, pet_id: int, new_name=None, new_age=None, new_breed=None):
        current = self.tree.root
        while current is not None:
            if current.pet.id == pet_id:
                if new_name:
                    current.pet.name = new_name
                if new_age:
                    current.pet.age = new_age
                if new_breed:
                    current.pet.breed = new_breed
                return {"message": "Pet updated successfully"}
            elif pet_id < current.pet.id:
                current = current.left
            else:
                current = current.right
        return {"error": "Pet not found"}
