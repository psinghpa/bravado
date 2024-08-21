
import pytest


@pytest.mark.xfail(reason="Deleting an existing pet always returns a 500")
def test_200_success(petstore):
    pets = petstore.pet.findPetsByStatus(status=['available']).result()
    if not pets:
        pytest.mark.xtail(reason="No pets to delete")
    pet_to_delete = pets.pop()
    result = petstore.pet.deletePet(petId=pet_to_delete.id).result()
    


@pytest.mark.xfail(reason="Don't know how to induce a 400")
def test_400_invalid_pet_value(petstore):
    result = petstore.pet.deletePet(petId=999).result()
    
