import os
from dotenv import load_dotenv

load_dotenv()

APP_ENV = os.getenv("APP_ENV", "dev")
IS_PROD = APP_ENV == "prod"
