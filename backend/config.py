import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
    AZURE_OPENAI_MODEL = os.getenv("AZURE_OPENAI_MODEL")
    AZURE_OPENAI_VERSION = os.getenv("AZURE_OPENAI_VERSION")

    COSMOS_URL = os.getenv("COSMOS_URL")
    COSMOS_KEY = os.getenv("COSMOS_KEY")
    COSMOS_DB = os.getenv("COSMOS_DB", "fitness")
    COSMOS_USER_CONTAINER = "users"
    COSMOS_LOGS_CONTAINER = "logs"

settings = Settings()
