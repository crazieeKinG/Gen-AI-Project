from dotenv import load_dotenv, get_key,find_dotenv
from app.core.services.logger.main import logger

load_dotenv()
env_path =find_dotenv()

def get_value(key: str) -> str:
    value = get_key(env_path, key)

    if value is None:
        return ""
    
    return value

OPENAI_API_KEY = get_value("OPENAI_API_KEY")
APP_USER_GUIDE_URL = get_value("APP_USER_GUIDE_URL")
