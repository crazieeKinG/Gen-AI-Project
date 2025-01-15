from app.data.datasource.app_user_guide_rag.main import pdf_retriever
from app.core.services.open_ai.main import llm
from app.core.constants.app_user_guide import pdf_document_prompt
from app.domain.app_user_guide.main import AppUserGuideResponse
from app.core.services.logger.main import logger

from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

logger.info("=== Initializing structured LLM and prompt template ===")

# Structured LLM
structured_llm = llm.with_structured_output(AppUserGuideResponse)

# Prompt template
pdf_template = ChatPromptTemplate.from_template(pdf_document_prompt)

# Runnables
pdf_rag_invoker = (
    {
        "pdf_context": pdf_retriever,
        "query": RunnablePassthrough(),
    }
    | pdf_template
    | structured_llm
)

logger.info("=== PDF rag invoker initialized successfully ===")
