import pytest

# Define the fixture
@pytest.fixture
def user_creds():
    def _user_creds(name: str, email: str, age: int, address: str, contact: str, gender: str):
        return {
            "name": name,
            "email": email,
            "age": age,
            "address": address,
            "contact": contact,
            "gender": gender,
        }
    return _user_creds

# Define the test
def test_user_creds(user_creds):
    assert user_creds(
        name="Abdullah",
        email="abdullah@gmail.com",
        age=23,
        address="Saima Arabian Villas",
        contact="0123456789",
        gender="male"
    ) == {
        "name": "Abdullah",
        "email": "abdullah@gmail.com",
        "age": 23,
        "address": "App Society",
        "contact": "0123456789",
        "gender": "male",
    }
    