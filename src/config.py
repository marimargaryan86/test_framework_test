from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Pydantic automatically looks for an environment variable named BASE_URL
    # or a key named BASE_URL inside your .env file.
    BASE_URL: str

    # If you want to add timeouts or thread counts later, Pydantic casts them automatically!
    # timeout: int = 30

    # Tell Pydantic to read from a .env file automatically
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


# Instantiate it once to expose it globally
Config = Settings()