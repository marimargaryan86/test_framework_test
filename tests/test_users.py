from src.models.user_model import UserModel
import pytest
from faker import Faker
import allure
fake = Faker()

@pytest.mark.smoke
@pytest.mark.user_management
@allure.feature("User Management")
def test_get_single_user_status_code(user_client):
    response = user_client.get_single_user(user_id=2)
    assert response.status_code == 200

@pytest.mark.smoke
@pytest.mark.user_management
@allure.feature("User Management")
def test_get_single_user_schema_and_data(user_client):
    response = user_client.get_single_user(user_id=2)
    response_data = response.json()

    # This line passes the raw dictionary into our Pydantic model.
    # It automatically checks that id is an int, name is a str, etc.
    user = UserModel(**response_data)

    # Now you can use clean object notation (user.name) instead of dict keys!
    assert user.name == "Ervin Howell"
    assert user.id == 2


@pytest.mark.smoke
@pytest.mark.user_management
@allure.feature("User Management")
@allure.story("Create User Account")
def test_create_user_with_dynamic_faker_data(user_client):
    # Use allure.step to log the chronological narrative of your test execution
    with allure.step("Arrange: Generate dynamic user payload using Faker"):
        fake_name = fake.name()
        fake_username = fake.user_name()
        fake_email = fake.email()

        payload = {
            "name": fake_name,
            "username": fake_username,
            "email": fake_email
        }

    with allure.step(f"Act: Send POST request to create user: {fake_name}"):
        response = user_client.create_user(payload)

    with allure.step("Assert: Verify response status code and data accuracy"):
        assert response.status_code == 201
        response_data = response.json()

        assert response_data["name"] == fake_name
        assert response_data["username"] == fake_username
        assert response_data["email"] == fake_email
        assert "id" in response_data