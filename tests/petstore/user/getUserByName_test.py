import pytest

@pytest.mark.skip("Yelp/bravado 's testcases itself are failing")
def test_200_success(petstore):
    result = petstore.user.getUserByName(username='bozo').result()
    assert petstore.get_model('User') == type(result)


@pytest.mark.xfail(reason='Returns 500 instead of 404')
def test_404_user_not_found(petstore):
    result = petstore.user.getUserByName(username='zzz').result()
    assert result is None


@pytest.mark.xfail(reason='Spec does not say what an invalid username is')
def test_400_invalid_username_supplied(petstore):
    result = petstore.user.getUserByName(username='').result()
    assert result is None
