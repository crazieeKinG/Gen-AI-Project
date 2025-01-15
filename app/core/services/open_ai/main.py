from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from app.core.constants.open_ai import OPENAI_API_KEY

# Initialize embeddings
embeddings = OpenAIEmbeddings(
    openai_api_key=OPENAI_API_KEY, model="text-embedding-ada-002"
)

# LLM model
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
