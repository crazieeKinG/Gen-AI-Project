from app.core.services.open_ai import pdf_loader
from app.core.services.open_ai.main import embeddings
from app.core.constants.app_user_guide import APP_USER_GUIDE_URL
from app.core.constants.open_ai import CHROMA_DB_DIR
from app.core.services.logger.main import logger

from langchain_chroma import Chroma

# Load the PDF document from the URL
pdf_documents = pdf_loader.load_pdf_file(APP_USER_GUIDE_URL)

# Initialize the vector db for the PDF
logger.info("=== Initializing vector db for app user guide ===")
pdf_vector_db = Chroma.from_documents(
    documents=pdf_documents,
    collection_name="app_user_guide",
    persist_directory=CHROMA_DB_DIR,
    embedding=embeddings,
)

# Initialize pdf vector db retriever
pdf_retriever = pdf_vector_db.as_retriever()

logger.info("=== PDF vector db initialized successfully ===")
