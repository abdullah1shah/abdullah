import pytest
import pandas as pd

# Function to read user data from the Excel file
def read_user_data_from_excel(file_path):
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(file_path)
    return df

# Fixture for user credentials
@pytest.fixture
def user_creds():
    def _user_creds(name: str, email: str, age: int, address: str, contact: str, gender: str):
        return {
            "name": name,
            "email": email,
            "age": age,
            "contact": contact,
            "gender": gender,
            "address": address 
        }
    return _user_creds

# Parameterized test with data from the Excel file
@pytest.mark.parametrize("user_data", read_user_data_from_excel("user_details.xlsx").to_dict(orient="records"))
def test_user_creds(user_creds, user_data):
    # Expected values
    expected_data = {
        "name": "Abdullah",
        "email": "abdullah@gmail.com",
        "age": 23,
        "contact": "123456789",
        "gender": "male",
        "address": "Gulshan Society"
    }
    # Now compare the actual data from Excel to the expected value
    assert user_creds(
        name=user_data["name"],
        email=user_data["email"],
        age=user_data["age"],
        contact=user_data["contact"],
        gender=user_data["gender"],
        address=user_data["address"]
    ) == expected_data