from pydantic import BaseModel


class UserModel(BaseModel):
    id: int
    name: str
    username: str
    email: str
    # Note: JSONPlaceholder users have nested fields like address and company,
    # but for this step we will just validate these 4 core top-level fields.
