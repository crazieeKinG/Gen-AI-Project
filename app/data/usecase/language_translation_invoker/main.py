from app.core.services.open_ai.main import llm
from app.core.constants.language_translation import translate_prompt
from app.domain.language_translation.main import LanguageTranslationResponse
from app.core.services.logger.main import logger

from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

logger.info(
    "=== Language Translation: Initializing structured LLM and prompt template ==="
)

# Structured LLM
structured_llm = llm.with_structured_output(LanguageTranslationResponse)

# Prompt template
translate_template = ChatPromptTemplate.from_template(translate_prompt)

# Runnables
translate_invoker = RunnablePassthrough() | translate_template | structured_llm

logger.info("=== Language Translation invoker initialized successfully ===")
