import pytest
@pytest.mark.skip("Yelp/bravado 's testcases itself are failing")
def test_200_success(petstore):
    User = petstore.get_model('User')
    users = [
        User(
            id=user_id,
            username='bozo',
            firstName='Bozo',
            lastName='Smith',
            email='bozo@clown.com',
            password='letmein',
            phone='111-222-3333',
            userStatus=3,
        ) for user_id in range(4)]

    result = petstore.user.createUsersWithArrayInput(body=users).result()
    assert result is None
