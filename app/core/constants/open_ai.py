from os import getenv
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = getenv("OPENAI_API_KEY")

CHROMA_DB_DIR = "chroma-db"
