from src.clients.base_client import BaseClient

class UserClient(BaseClient):

    def get_single_user(self, user_id: int):
        """Fetches a single user by their ID."""
        return self._get(f"/users/{user_id}")

    def create_user(self, user_payload: dict):
        return self._post("/users", user_payload)