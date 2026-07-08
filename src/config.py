import os
from dotenv import load_dotenv

# Load the variables from the .env file
load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL")

    # We can add a fallback error just in case we forget to set it in .env
    if not BASE_URL:
        raise ValueError("BASE_URL is not set in the environment or .env file!")