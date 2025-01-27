from app.core.constants.env import OPENAI_API_KEY
from app.core.services.logger.main import logger

from langchain_openai import OpenAIEmbeddings, ChatOpenAI


# Initialize embeddings
embeddings = OpenAIEmbeddings(
    openai_api_key=OPENAI_API_KEY, model="text-embedding-ada-002"
)

# LLM model
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

logger.info("=== Initializing embeddings and LLM model ===")
