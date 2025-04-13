from model.abb import ABB
from model.pet import Pet

class ABBService:
    def __init__(self):
        self.tree = ABB()
        # Datos de ejemplo
        self.tree.add(Pet(id=10, name="Bobby", age=4, breed="golden retriever", locality="Bogotá", gender="Male"))
        self.tree.add(Pet(id=3, name="Max", age=6, breed="bulldog", locality="Medellín", gender="Male"))

    def add_pet(self, pet: Pet):
        if self.check_pet_exists(pet.id):
            return {"error": "A pet with this ID already exists."}
        self.tree.add(pet)
        return {"message": "Pet added successfully"}

    def check_pet_exists(self, pet_id: int):
        current = self.tree.root
        while current:
            if current.pet.id == pet_id:
                return True
            current = current.left if pet_id < current.pet.id else current.right
        return False

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
            while node.left:
                node = node.left
            return node

        if not self.check_pet_exists(pet_id):
            return {"error": "Pet not found"}

        self.tree.root = delete(self.tree.root, pet_id)
        return {"message": "Pet removed successfully"}

    def update_pet_info(self, pet_id: int, new_name=None, new_age=None, new_breed=None):
        current = self.tree.root
        while current:
            if current.pet.id == pet_id:
                if new_name: current.pet.name = new_name
                if new_age: current.pet.age = new_age
                if new_breed: current.pet.breed = new_breed
                return {"message": "Pet updated successfully"}
            current = current.left if pet_id < current.pet.id else current.right
        return {"error": "Pet not found"}

    def get_all_inorder(self):
        return self.tree.inorder()

    def get_all_preorder(self):
        return self.tree.preorder()

    def get_all_postorder(self):
        return self.tree.postorder()

    def get_pets_by_breed(self, breed: str):
        result = []

        def search(node):
            if node:
                if node.pet.breed.lower() == breed.lower():
                    result.append(node.pet)
                search(node.left)
                search(node.right)

        search(self.tree.root)
        if not result:
            return {"error": "No pets found for this breed"}
        return {"pets": result}

    def get_pet_by_id(self, pet_id: int):
        current = self.tree.root
        while current:
            if current.pet.id == pet_id:
                return current.pet
            current = current.left if pet_id < current.pet.id else current.right
        return None

    def get_pets_by_locality(self, locality: str):
        result = []

        def search(node):
            if node:
                if node.pet.locality.lower() == locality.lower():
                    result.append(node.pet)
                search(node.left)
                search(node.right)

        search(self.tree.root)
        if not result:
            return {"error": "No pets found for this locality"}
        return {"pets": result}

    def get_pets_by_gender(self, gender: str):
        result = []

        def search(node):
            if node:
                if node.pet.gender.lower() == gender.lower():
                    result.append(node.pet)
                search(node.left)
                search(node.right)

        search(self.tree.root)
        if not result:
            return {"error": "No pets found for this gender"}
        return {"pets": result}

    def get_report_by_locality_and_gender(self):
        report = {}

        def traverse(node):
            if node:
                pet = node.pet
                locality = pet.locality
                gender = pet.gender

                if locality not in report:
                    report[locality] = {}

                if gender not in report[locality]:
                    report[locality][gender] = 0

                report[locality][gender] += 1

                traverse(node.left)
                traverse(node.right)

        traverse(self.tree.root)
        return report
