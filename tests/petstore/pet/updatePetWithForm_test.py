
import pytest

@pytest.mark.skip("Yelp/bravado 's testcases itself are failing")
def test_success(petstore):
    result = petstore.pet.updatePetWithForm(
        petId='1',
        name='darwin',
        status='available').result()
    print(result)
    assert result


@pytest.mark.xfail(reason="Don't know now to cause a 405")
def test_405_invalid_input():
    assert False
