from app.data.datasource.app_user_guide_rag.main import pdf_retriever
from app.core.services.open_ai.main import llm
from app.core.constants.app_user_guide import pdf_document_prompt
from app.core.constants.language_translation import translate_prompt
from app.domain.app_user_guide.main import AppUserGuideResponse
from app.core.services.logger.main import logger
from app.feature.language_translation.main import translate_invoker

from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
import ast

logger.info("=== App User Guide: Initializing structured LLM and prompt template ===")

# Structured LLM
structured_llm = llm.with_structured_output(AppUserGuideResponse)

# Prompt template
pdf_template = ChatPromptTemplate.from_template(pdf_document_prompt)
translate_template = ChatPromptTemplate.from_template(translate_prompt)

# Runnables
rag_invoker = (
    {
        "pdf_context": pdf_retriever,
        "query": RunnablePassthrough(),
    }
    | pdf_template
    | structured_llm
)


def pdf_rag_invoker(query: str, target_lang: str):
    """
    Function to invoke the PDF retrieval and response generation process.

    Also, translate the response to the target language.
    """
    rag_response = rag_invoker.invoke(query)

    translate_response = translate_invoker.invoke(
        {"text": str(rag_response.dict()), "target_language": target_lang}
    )

    if translate_response.source_lang == translate_response.target_lang:
        return rag_response

    rag_response.translated_response = ast.literal_eval(translate_response.response)

    return rag_response


logger.info("=== App User Guide PDF rag invoker initialized successfully ===")
