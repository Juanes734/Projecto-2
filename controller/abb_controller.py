from fastapi import APIRouter, HTTPException, status
from model.pet import Pet
from service.abb_service import ABBService

abb_service = ABBService()
abb_route = APIRouter(prefix="/abb", tags=["ABB"])

# Obtener mascotas en distintos recorridos del árbol
@abb_route.get("/inorder")
async def inorder():
    return {"pets": abb_service.get_all_inorder()}

@abb_route.get("/preorder")
async def preorder():
    return {"pets": abb_service.get_all_preorder()}

@abb_route.get("/postorder")
async def postorder():
    return {"pets": abb_service.get_all_postorder()}

# Obtener todas las mascotas
@abb_route.get("/")
async def get_all_pets():
    pets = abb_service.get_all_inorder()
    if not pets:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No pets found")
    return {"pets": pets}

# Obtener mascota por ID
@abb_route.get("/{pet_id}")
async def get_pet_by_id(pet_id: int):
    pet = abb_service.get_pet_by_id(pet_id)
    if pet is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pet not found")
    return {"pet": pet}

# Agregar nueva mascota
@abb_route.post("/pets")
def add_pet(pet: Pet):
    try:
        return abb_service.add_pet(pet)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Actualizar mascota existente
@abb_route.put("/{pet_id}")
async def update_pet(pet_id: int, updated_pet: Pet):
    result = abb_service.update_pet_info(pet_id, updated_pet.name, updated_pet.age, updated_pet.breed)
    if "error" in result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=result["error"])
    return result

# Eliminar mascota
@abb_route.delete("/{pet_id}")
async def delete_pet(pet_id: int):
    result = abb_service.remove_pet(pet_id)
    if "error" in result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=result["error"])
    return result

# Filtros por atributos
@abb_route.get("/breed/{breed}")
async def get_pets_by_breed(breed: str):
    result = abb_service.get_pets_by_breed(breed)
    if "error" in result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=result["error"])
    return result

@abb_route.get("/locality/{locality}")
async def get_pets_by_locality(locality: str):
    result = abb_service.get_pets_by_locality(locality)
    if "error" in result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=result["error"])
    return result

@abb_route.get("/gender/{gender}")
async def get_pets_by_gender(gender: str):
    result = abb_service.get_pets_by_gender(gender)
    if "error" in result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=result["error"])
    return result

# Reporte cruzado por localidad y género
@abb_route.get("/report/location-gender")
async def get_report_by_location_and_gender():
    return abb_service.get_report_by_locality_and_gender()
